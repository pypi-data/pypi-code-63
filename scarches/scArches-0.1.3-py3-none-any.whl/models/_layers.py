from keras import backend as K
from keras.engine import Layer
from keras.layers import Dense
from keras import initializers, regularizers, constraints


class SliceLayer(Layer):
    def __init__(self, index=0, **kwargs):
        self.index = index
        super().__init__(**kwargs)

    def build(self, input_shape):
        if not isinstance(input_shape, list):
            raise ValueError('Input should be a list')

        super().build(input_shape)

    def call(self, x, **kwargs):
        assert isinstance(x, list), 'SliceLayer input is not a list'
        return x[self.index]

    def compute_output_shape(self, input_shape):
        return input_shape[self.index]


class ColwiseMultLayer(Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self, input_shape):
        if not isinstance(input_shape, list):
            raise ValueError('Input should be a list')

        super().build(input_shape)

    def call(self, x, **kwargs):
        assert isinstance(x, list), 'SliceLayer input is not a list'
        return x[0] * K.reshape(x[1], (-1, 1))

    def compute_output_shape(self, input_shape):
        return input_shape[0]


class FirstLayer(Layer):
    def __init__(self, units=128, kernel_initializer='glorot_uniform', kernel_regularizer=None, use_bias=False,
                 freeze=False, bias_initializer='zeros', bias_regularizer=None, bias_constraint=None, **kwargs):
        self.units = units
        self.kernel_initializer = kernel_initializer
        self.kernel_regularizer = kernel_regularizer
        self.use_bias = use_bias
        self.freeze = freeze

        self.bias_initializer = bias_initializer
        self.bias_regularizer = bias_regularizer
        self.bias_constraint = bias_constraint
        super().__init__(**kwargs)
        Dense

    def build(self, input_shape):
        if not isinstance(input_shape, list):
            raise ValueError('Input shape should be a list')

        assert len(input_shape) >= 2

        self.expression_kernel = self.add_weight(shape=(input_shape[0][-1], self.units),
                                                 initializer=self.kernel_initializer,
                                                 name='expression_kernel',
                                                 regularizer=self.kernel_regularizer,
                                                 trainable=not self.freeze)

        self.condition_kernel = self.add_weight(shape=(input_shape[1][-1], self.units),
                                                initializer=self.kernel_initializer,
                                                name='condition_kernel',
                                                regularizer=self.kernel_regularizer,
                                                trainable=True)

        if len(input_shape) == 3:
            self.cell_type_kernel = self.add_weight(shape=(input_shape[2][-1], self.units),
                                                    initializer=self.kernel_initializer,
                                                    name='cell_type_kernel',
                                                    regularizer=self.kernel_regularizer,
                                                    trainable=True)

        if self.use_bias:
            self.bias = self.add_weight(shape=(self.units,),
                                        initializer=self.bias_initializer,
                                        name='bias',
                                        regularizer=self.bias_regularizer,
                                        constraint=self.bias_constraint)
        else:
            self.bias = None

        super().build(input_shape)

    def call(self, inputs, **kwargs):
        if not isinstance(inputs, list):
            raise ValueError('Inputs should be a list')

        genes_output = K.dot(inputs[0], self.expression_kernel)
        condition_output = K.dot(inputs[1], self.condition_kernel)
        
        if len(inputs) == 3:
            cell_type_output = K.dot(inputs[2], self.cell_type_kernel)
        else:
            cell_type_output = K.zeros_like(condition_output)
        
        output = genes_output + condition_output + cell_type_output
        if self.use_bias:
            output = K.bias_add(output, self.bias, data_format='channels_last')

        return output

    def compute_output_shape(self, input_shape):
        if not isinstance(input_shape, list):
            raise ValueError('Input shape should be a list')

        assert len(input_shape) >= 2

        return (input_shape[0][0], self.units)

    def get_config(self):
        base_config = super(FirstLayer, self).get_config()
        config = {}
        config['units'] = self.units
        config['kernel_initializer'] = initializers.serialize(self.kernel_initializer)
        config['kernel_regularizer'] = regularizers.serialize(self.kernel_regularizer)
        config['use_bias'] = self.use_bias
        config['bias_initializer'] = self.bias_initializer
        config['bias_regularizer'] = self.bias_regularizer
        config['bias_constraint'] = constraints.serialize(self.bias_constraint)
        return dict(list(base_config.items()) + list(config.items()))
        

LAYERS = {
    "SliceLayer": SliceLayer,
    "ColWiseMultLayer": ColwiseMultLayer,
    "FirstLayer": FirstLayer,
}
