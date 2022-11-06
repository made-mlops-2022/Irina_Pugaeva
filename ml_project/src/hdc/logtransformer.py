import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class LogTransformer(BaseEstimator, TransformerMixin):
    """
    Log transforming
    """

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.log(np.abs(X) + 1)

    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X, y)