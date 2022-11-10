import pathlib
import unittest

import numpy as np
from hdc.trainer import Trainer
from sklearn.model_selection import GridSearchCV
from sklearn.utils.validation import check_is_fitted

from data_generator import generate_fake_dataset

default_cfg_path = pathlib.Path(".") / "configs" / "train_svm_033.json"

class Test(unittest.TestCase):

    def test_model_isinstance_gridsearch(self):
        trainer = Trainer(default_cfg_path)
        self.assertIsInstance(trainer.gs, GridSearchCV)

    def test_fit(self):
        trainer = Trainer(default_cfg_path)
        df = generate_fake_dataset()
        X_train, y_train, X_test, y_test = trainer.split_data(df)
        trainer.fit(X_train, y_train)
        self.assertIsNone(check_is_fitted(trainer.gs))

    def test_predict(self):
        trainer = Trainer(default_cfg_path)
        df = generate_fake_dataset()
        X_train, y_train, X_test, y_test = trainer.split_data(df)
        trainer.fit(X_train, y_train)
        trainer.predict(X_test)
        self.assertEqual(y_test.shape[0], trainer.predict(X_test).shape[0])