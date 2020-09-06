"""
torch interface
"""

import os
import time
from magic import LOG_INFO
from magic.data import DataLoader
from magic import Estimator

import torch
from torch.optim import lr_scheduler
from torchsummary import summary
from torch.utils.tensorboard import SummaryWriter

class TorchEstimator(Estimator):
    """ torch estimator """

    def __init__(self, config):

        self.cfg = config

        # check cuda
        self.device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        self.current_epoch = 0

        # fake model as estimator interface, need a actual
        model = torch.nn.Module()
        self.model = torch.nn.DataParallel(model)
        self.model.to(self.device)

    def summary(self):
        """
        support multiple inputs to the network
        :param inputs_size, list of size, don't contain batch size: [[C, H, W], [C, H, W], ...]
        """
        inputs_size = [tuple(size) for size in self.cfg.inputs_size]  # need tuple type

        self.summary_writer = SummaryWriter()  # tensorboard

        self.model.to(self.device)

        # add graph to tensorboard
        batch = 1
        dummy_inputs = tuple([torch.randn(batch, *size).to(self.device) for size in inputs_size])
        torch_model = self.model.module if hasattr(self.model, "module") else self.model
        self.summary_writer.add_graph(torch_model, dummy_inputs)
        self.summary_writer.flush()

        LOG_INFO("model summary .. ")
        summary(torch_model, inputs_size, batch_size=batch, device=self.device.type)

    def load(self, strict=False):
        """
        Partially loading a model or loading a partial model are common scenarios
        when transfer learning or training a new complex model. Leveraging trained parameters,
        even if only a few are usable, will help to warmstart the training process and
        hopefully help your model converge much faster than training from scratch.
        you can set the strict argument to False in the load_state_dict() function to ignore non-matching keys
        """
        pre_trained = self.cfg.pre_trained

        LOG_INFO("loading pre_trained model ... ")
        self.model.to(self.device)
        checkpoint = torch.load(pre_trained, map_location=self.device)
        if hasattr(self.model, "module"):
            self.model.module.load_state_dict(checkpoint, strict=strict)
        else:
            self.model.load_state_dict(checkpoint, strict=strict)

    def save(self, model_path=None):
        """ save model """
        if model_path is None:
            model_path = self.cfg.pre_trained

        """
        torch.nn.DataParallel is a model wrapper that enables parallel GPU utilization.
        To save a DataParallel model generically, save the model.module.state_dict(). 
        This way, you have the flexibility to load the model any way you want to any device you want.
        """

        if hasattr(self.model, "module"):
            if len(self.model.module.state_dict()) == 0:
                raise RuntimeError("model is empty")
            torch.save(self.model.module.state_dict(), model_path)
        else:
            if len(self.model.state_dict()) == 0:
                raise RuntimeError("model is empty")
            torch.save(self.model.state_dict(), model_path)
        LOG_INFO("saved to {}".format(model_path))

    def export_model(self):
        """
        Exporting a model in PyTorch works via tracing or scripting.
        To export a model, we call the torch.onnx.export() function.
        This will execute the model, recording a trace of what operators are used to compute the outputs.
        Because export runs the model, we need to provide an input tensor x.
        The values in this can be random as long as it is the right type and size.

        inputs_size, list of size, [[C, H, W], [C, H, W], ...]
        :param opset_version: onnx version
        :param batch: for onnx batch
        :param input_names: can ignore
        :param output_names: can ignore
        """

        import onnx
        from onnxsim import simplify

        # Export the model
        self.model.to(self.device)  # set the model to inference mode
        self.model.eval()

        dummy_inputs = tuple([torch.randn(self.cfg.onnx_batch, *size).to(self.device) for size in self.cfg.inputs_size])

        torch_model = self.model.module if hasattr(self.model, "module") else self.model

        torch.onnx.export(torch_model,  # model being run
                          dummy_inputs,  # model input (or a tuple for multiple inputs)
                          self.cfg.onnx_path,  # where to save the model (can be a file or file-like object)
                          export_params=True,  # store the trained parameter weights inside the model file
                          opset_version=self.cfg.opset_version,  # the ONNX version to export the model to
                          do_constant_folding=True,  # whether to execute constant folding for optimization
                          input_names=self.cfg.input_names,  # the model's input names
                          output_names=self.cfg.output_names,  # the model's output names
                          verbose=self.cfg.export_onnx_verbose
                          )

        # load your predefined ONNX model
        onnx_model = onnx.load(self.cfg.onnx_path)
        onnx_model, check = simplify(onnx_model)
        assert check, "Simplified ONNX model could not be validated"
        onnx.save(onnx_model, self.cfg.onnx_path)
        LOG_INFO("onnx saved to: {}".format(self.cfg.onnx_path))

    def backward_optim(self, train_dataset=None, loss_fn=None, optimizer=None, scheduler=None):
        """train process
        :param train_dataset: train dataset
        :param loss_fn: loss_fn(model, data)
        :param optimizer: SGD ...
        :param scheduler: if None, use CosineAnnealingLR
        """

        # Releases all unoccupied cached memory currently held by the caching allocator
        # so that those can be used in other GPU application and visible in nvidia-smi.
        torch.cuda.empty_cache()

        self.model.to(self.device)
        self.model.train()

        assert train_dataset, "need train dataset"
        assert loss_fn, "need loss function"
        assert optimizer, "need optimizer to update parameters"
        if scheduler is None:
            scheduler = lr_scheduler.CosineAnnealingLR(optimizer, T_max=self.cfg.epoch_range[1])

        self.summary()

        LOG_INFO("training ...")
        n_samples_train = len(train_dataset)
        steps_per_epoch = (n_samples_train + self.cfg.train_batch - 1) // self.cfg.train_batch
        LOG_INFO("n_samples_train: {}".format(n_samples_train))

        train_loader = DataLoader(dataset=train_dataset,
                                  batch_size=self.cfg.train_batch,
                                  num_workers=self.cfg.num_workers)

        running_loss = 0.0
        time_stamp0 = time.time()
        model_backup_list = []  # record model path saved already
        for epoch in range(*self.cfg.epoch_range[:2]):
            self.current_epoch = epoch

            # print learning rate every epoch
            lr = optimizer.state_dict()["param_groups"][0]["lr"]
            self.summary_writer.add_scalar("train/learning rate", lr, epoch + 1)
            self.summary_writer.flush()

            for i, sample in enumerate(train_loader, 0):
                # zero the parameter gradients
                optimizer.zero_grad()

                # forward + backward + optimize
                loss = loss_fn(self.model, sample)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()

                # print by steps
                if i % self.cfg.loss_avg_step == self.cfg.loss_avg_step - 1:
                    step = i + 1
                    global_step = epoch * steps_per_epoch + step
                    # calculate time consume
                    time_stamp1 = time.time()
                    time_consume_per_step = (time_stamp1 - time_stamp0) / self.cfg.loss_avg_step
                    time_stamp0 = time_stamp1
                    remain = (steps_per_epoch - step) * time_consume_per_step
                    # average loss
                    running_loss_avg = running_loss / self.cfg.loss_avg_step

                    LOG_INFO("epoch:{} step:{}/{} remain:{:.0f}s loss:{:.6f} lr:{}".format(epoch + 1, step, steps_per_epoch, remain, running_loss_avg, lr))
                    # print loss to tensorboard
                    self.summary_writer.add_scalar('train/loss', running_loss_avg, global_step)
                    self.summary_writer.flush()
                    running_loss = 0.0

            # do something by epoch frequency
            if epoch % self.cfg.epoch_range[2] == self.cfg.epoch_range[2] - 1:
                # save model by epoch interval
                path_bak = self.cfg.pre_trained + "_epoch{}".format(epoch + 1)
                self.save(path_bak)
                model_backup_list.append(path_bak)
                assert self.cfg.model_backup_upper > 0
                if len(model_backup_list) > self.cfg.model_backup_upper:
                    try:
                        os.remove(model_backup_list.pop(0))
                    except Exception as err:
                        print(err)

                # visualize model weights histogram
                try:
                    for name, params in self.model.named_parameters():
                        self.summary_writer.add_histogram(name, params, epoch + 1)
                    self.summary_writer.flush()
                except Exception as err:
                    print(err)

                try:
                    self.model.eval()
                    self.eval()
                    self.model.train()

                except Exception as err:
                    print(err)

            # adjust learning rate every epoch
            scheduler.step()

        # exit from training
        self.summary_writer.close()
