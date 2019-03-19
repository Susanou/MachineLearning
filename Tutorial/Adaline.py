#!/usr/bin/python3

import numpy as np

class AdalineGD(object):
    """ADAptive NEuron classifier

    Parameters:

    eta: float
        Learning rate (between 0.0 & 1.0)
    n_iter:
        Number of times go over the training data
    
    Attributes:
    
    w_: 1D array
        weights after fitting
    errors_: list
        Number of mussclassifications in each epoch

    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        """Fitting of the data

        Parameters:

        X: {array-like}, shape = [n_samples, n_features]
            Training vectors
            where n_samples = number of samples in the data
                  n_features = number of features measured
        y: array-like, shape = [n_samples]
            Target values

        Returns:

        self: object
        """

        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        
        return self

    def net_input(self, X):
        """Calculate the net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def activation(self, X):
        """Compute the linear activation"""
        return self.net_input(X)
    
    def predict(self, X):
        """Return class label after unit setp"""
        return np.where(self.activation(X) >= 0.0, 1, -1)