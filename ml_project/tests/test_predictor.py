import pathlib
import unittest

import numpy as np
from hdc.predictor import Predictor

from data_generator import generate_fake_dataset

default_cfg_path = pathlib.Path(".") / "configs" / "predict.json"

class Test(unittest.TestCase):

    def test_predict(self):
        predictor = Predictor(default_cfg_path)
        data = predictor.load_data()
        predictions = predictor.predict(data)
        self.assertIsInstance(predictions, np.ndarray)
