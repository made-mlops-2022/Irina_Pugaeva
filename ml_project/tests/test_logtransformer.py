import unittest
import numpy as np

from hdc.logtransformer import LogTransformer

class Test(unittest.TestCase):
    def test_log_transformer(self):
        X = np.array([[1, 1, 1], [0, -2, 1.5]])
        expected_X = np.log(np.abs(X) + 1)
        lt = LogTransformer()
        self.assertTrue(np.allclose(expected_X, lt.fit_transform(X)))