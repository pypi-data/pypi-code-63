
# Authors: Thierry Moudiki
#
# License: BSD 3 Clear


import pickle 
import numpy as np
import sklearn.metrics as skm2
from .glm import GLM
from ..utils import matrixops as mo
from ..utils import misc as mx
from sklearn.base import RegressorMixin
from scipy.optimize import minimize
from ..optimizers import Optimizer
from scipy.special import erf, factorial


class GLMRegressor(GLM, RegressorMixin):
    """Generalized 'linear' models using quasi-randomized networks (regression)
    
        Parameters
       ----------
       n_hidden_features: int
           number of nodes in the hidden layer
       lambda1: float
           regularization parameter for GLM coefficients on original features
       alpha1: float
           controls compromize between l1 and l2 norm of GLM coefficients on original features
       lambda2: float
           regularization parameter for GLM coefficients on nonlinear features
       alpha2: float
           controls compromize between l1 and l2 norm of GLM coefficients on nonlinear features
       activation_name: str
           activation function: 'relu', 'tanh', 'sigmoid', 'prelu' or 'elu'
       a: float
           hyperparameter for 'prelu' or 'elu' activation function
       nodes_sim: str
           type of simulation for the nodes: 'sobol', 'hammersley', 'halton', 
           'uniform'
       bias: boolean
           indicates if the hidden layer contains a bias term (True) or not 
           (False)
       dropout: float
           regularization parameter; (random) percentage of nodes dropped out 
           of the training
       direct_link: boolean
           indicates if the original predictors are included (True) in model's 
           fitting or not (False)
       n_clusters: int
           number of clusters for 'kmeans' or 'gmm' clustering (could be 0: 
               no clustering)
       cluster_encode: bool
           defines how the variable containing clusters is treated (default is one-hot)
           if `False`, then labels are used, without one-hot encoding
       type_clust: str
           type of clustering method: currently k-means ('kmeans') or Gaussian 
           Mixture Model ('gmm')
       type_scaling: a tuple of 3 strings
           scaling methods for inputs, hidden layer, and clustering respectively
           (and when relevant). 
           Currently available: standardization ('std') or MinMax scaling ('minmax')
       optimizer: object 
           optimizer, from class nnetsauce.utils.Optimizer
       seed: int 
           reproducibility seed for nodes_sim=='uniform'
    """
    
    
    # construct the object -----

    def __init__(
        self,        
        n_hidden_features=5,
        lambda1=0.01,
        alpha1=0.5,
        lambda2=0.01,
        alpha2=0.5,
        family="gaussian",
        activation_name="relu",
        a=0.01,
        nodes_sim="sobol",
        bias=True,
        dropout=0,
        direct_link=True,
        n_clusters=2,
        cluster_encode=True,
        type_clust="kmeans",
        type_scaling=("std", "std", "std"),  
        optimizer=Optimizer(),
        seed=123,
    ):

        super().__init__(
            n_hidden_features=n_hidden_features,
            lambda1=lambda1,
            alpha1=alpha1,
            lambda2=lambda2,
            alpha2=alpha2,
            activation_name=activation_name,
            a=a,
            nodes_sim=nodes_sim,
            bias=bias,
            dropout=dropout,
            direct_link=direct_link,
            n_clusters=n_clusters,
            cluster_encode=cluster_encode,
            type_clust=type_clust,
            type_scaling=type_scaling,
            optimizer=optimizer,
            seed=seed,
        )
        
        self.family = family
     
        
     
    def gaussian_loss(self, y, row_index, XB):
        return 0.5*np.mean(np.square(y[row_index] - XB))
        
    
    def laplace_loss(self, y, row_index, XB):
        return 0.5*np.mean(np.abs(y[row_index] - XB))

    
    def loglik_zip(beta, group_index, X, y, zero_mass, 
               lambda1, alpha1, lambda2, alpha2, 
               intercept=True):

        max_double = 709.0
        zero = np.finfo(float).eps
        not_zero_mass = 1 - zero_mass
        n = len(y)
    
        if intercept:
    
            XB = np.minimum(np.dot(np.column_stack((np.repeat(1, n), X)), beta), 
                            max_double) # (!) stack columns outside loglik
            
            mu = np.minimum(np.exp(XB), 
                          max_double) # avoid overflows  # but...
        
            exp_mu = np.exp(-mu)
            not_zero_mass_exp_mu = not_zero_mass*exp_mu
        
            f = (y == 0)*(zero_mass + not_zero_mass_exp_mu) \
            + (y > 0)*(not_zero_mass_exp_mu * np.power(mu, y)/factorial(y))   
        
            return -np.mean(np.log(np.maximum(f, zero)))
        
        else:
    
            XB = np.minimum(np.dot(X, beta), 
                              max_double) # avoid overflows  # but...
            
            mu = np.minimum(np.exp(XB), 
                          max_double) # avoid overflows # but...
        
            exp_mu = np.exp(-mu)
            not_zero_mass_exp_mu = not_zero_mass*exp_mu
        
            f = (y == 0)*(zero_mass + not_zero_mass_exp_mu) \
            + (y > 0)*(not_zero_mass_exp_mu * np.power(mu, y)/factorial(y))   
        
            return -np.mean(np.log(np.maximum(f, zero))) 
    

    def loglik_poisson(beta, group_index, X, y, 
                       lambda1, alpha1, lambda2, alpha2, 
                       intercept=True):
      
        max_double = 709.0
        zero = np.finfo(float).eps
        n = len(y)
    
        if intercept:
    
            XB = np.minimum(np.dot(np.column_stack((np.repeat(1, n), X)), beta), 
                            max_double) # (!) stack columns outside loglik
            
            mu = np.minimum(np.exp(XB), 
                          max_double) # avoid overflows # but...
        
            f = np.exp(-mu)*np.power(mu, y)/factorial(y)
        
            return -np.mean(np.log(np.maximum(f, zero)))
        
        else:
    
            XB = np.minimum(np.dot(X, beta), 
                              max_double) # avoid overflows # but...
            
            mu = np.minimum(np.exp(XB), 
                          max_double) # avoid overflows # but...
        
            f = np.exp(-mu)*np.power(mu, y)#/factorial(y)
        
            return -np.mean(np.log(np.maximum(f, zero)))
        
    
    def loglik_nbinom(beta, group_index, X, y, 
                      lambda1, alpha1, lambda2, alpha2, 
                      intercept=True):
      
      max_double = 709.0
      zero = np.finfo(float).eps
      n = len(y)
    
      if intercept:
        
        XB = np.minimum(np.dot(np.column_stack((np.repeat(1, n), X)), beta), 
                        max_double) # (!) stack columns outside loglik
    
        p_hat = 0.5*(1 + erf(1.0/(XB/n + 1.0)))
    
        f = factorial(y+n-1)/(factorial(n-1)*factorial(y))*np.power(p_hat, n)*np.power(1-p_hat, y) # nbinom.pmf(y, n, p_hat, loc=0)
    
        return -np.mean(np.log(np.maximum(f, zero)))
    
      else:
      
        XB = np.minimum(np.dot(X, beta), 
                        max_double) # avoid overflows
        
        p_hat = 0.5*(1 + erf(1.0/(XB/n + 1.0)))
    
        f = factorial(y+n-1)/(factorial(n-1)*factorial(y))*np.power(p_hat, n)*np.power(1-p_hat, y) # nbinom.pmf(y, n, p_hat, loc=0)
    
        return -np.mean(np.log(np.maximum(f, zero)))
    
    
    
    def loss_func(self, beta, group_index, X, y, 
                  row_index=None, type_loss="gaussian", 
                  **kwargs):

        res = {"gaussian": self.gaussian_loss,
               "laplace": self.laplace_loss}
        
        if row_index is None:            
            
            row_index = range(len(y))
            XB = self.compute_XB(X, beta=beta)  

            return res[type_loss](y, row_index, XB) + self.compute_penalty(group_index=group_index, 
                  beta=beta)              
            
        XB = self.compute_XB(X, beta=beta, 
                             row_index=row_index)                
        
        return res[type_loss](y, row_index, XB) + self.compute_penalty(group_index=group_index, 
                  beta=beta)                                          
        
                                                
    
    def fit(self, X, y, 
            learning_rate=0.01, decay=0.1, # in an object, in constructor
            batch_prop=1, tolerance=1e-5, # in an object, in constructor
            optimizer = None, # in an object, in constructor
            verbose=0, **kwargs):
        """Fit GLM model to training data (X, y).
        
        Parameters
        ----------
        X: {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number 
            of samples and n_features is the number of features.
        
        y: array-like, shape = [n_samples]
               Target values.
    
        **kwargs: additional parameters to be passed to 
                  self.cook_training_set or self.obj.fit
               
        Returns
        -------
        self: object
        """
        
        self.beta = None
        
        self.n_iter = 0
        
        n, self.group_index = X.shape
        
        centered_y, scaled_Z = self.cook_training_set(y=y, X=X)
        
        n_Z = scaled_Z.shape[0]
        
        # initialization                    
        beta_ = np.linalg.lstsq(scaled_Z, centered_y, rcond=None)[0]     

        self.optimizer.learning_rate = learning_rate
        self.optimizer.decay = decay
        self.optimizer.batch_prop = batch_prop
        self.optimizer.verbose = verbose
         
        
        # optimization
        # fit(self, loss_func, response, x0, **kwargs):
        # loss_func(self, beta, group_index, X, y, 
        #          row_index=None, type_loss="gaussian", 
        #          **kwargs)
        self.optimizer.fit(self.loss_func,  
                           response = centered_y, 
                           x0 = beta_,
                           group_index = self.group_index, 
                           X = scaled_Z, 
                           y = centered_y, 
                           type_loss=self.family, 
                           tolerance=tolerance,
                           **kwargs)         

        self.beta = self.optimizer.results[0]
        
        return self
    
    
    
    def predict(self, X, **kwargs):
        """Predict test data X.
        
        Parameters
        ----------
        X: {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number 
            of samples and n_features is the number of features.
        
        **kwargs: additional parameters to be passed to 
                  self.cook_test_set
               
        Returns
        -------
        model predictions: {array-like}        
        """
        
        if len(X.shape) == 1:

            n_features = X.shape[0]
            new_X = mo.rbind(
                X.reshape(1, n_features),
                np.ones(n_features).reshape(1, n_features),
            )
                           
            return (self.y_mean + np.dot(self.cook_test_set(new_X, **kwargs), 
                                         self.beta))[0]
        
        return self.y_mean + np.dot(self.cook_test_set(X, **kwargs), 
                                    self.beta)
    
    
    
    def score(self, X, y, scoring=None, **kwargs):
        """ Score the model on test set features X and response y. 

        Parameters
        ----------
        X: {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number 
            of samples and n_features is the number of features

        y: array-like, shape = [n_samples]
            Target values

        scoring: str
            must be in ('explained_variance', 'neg_mean_absolute_error', \
                        'neg_mean_squared_error', 'neg_mean_squared_log_error', \
                        'neg_median_absolute_error', 'r2')
        
        **kwargs: additional parameters to be passed to scoring functions
               
        Returns
        -------
        model scores: {array-like}
        """

        preds = self.predict(X)

        if type(preds) == tuple:  # if there are std. devs in the predictions
            preds = preds[0]

        if scoring is None:
            scoring = "neg_mean_squared_error"

        # check inputs
        assert scoring in (
            "explained_variance",
            "neg_mean_absolute_error",
            "neg_mean_squared_error",
            "neg_mean_squared_log_error",
            "neg_median_absolute_error",
            "r2",
        ), "'scoring' should be in ('explained_variance', 'neg_mean_absolute_error', \
                           'neg_mean_squared_error', 'neg_mean_squared_log_error', \
                           'neg_median_absolute_error', 'r2')"

        scoring_options = {
            "explained_variance": skm2.explained_variance_score,
            "neg_mean_absolute_error": skm2.mean_absolute_error,
            "neg_mean_squared_error": skm2.mean_squared_error,
            "neg_mean_squared_log_error": skm2.mean_squared_log_error,
            "neg_median_absolute_error": skm2.median_absolute_error,
            "r2": skm2.r2_score,
        }

        return scoring_options[scoring](y, preds, **kwargs)