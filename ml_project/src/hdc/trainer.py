import json
import os
import pickle
from time import time

import pandas as pd
import sklearn
from hydra.utils import instantiate
from omegaconf import OmegaConf
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline

from hdc.logtransformer import LogTransformer
from hdc.utils.config import TrainConfig
from hdc.utils.logger import logger


class Trainer:
    def __init__(self, cfg_path) -> None:
        with open(cfg_path) as cfg_file:
            cgf_dict = json.load(cfg_file)
        self.cfg = TrainConfig.from_dict(cgf_dict)
        self.cfg = instantiate(self.cfg)
        self.RS = self.cfg.data_params['random_state']
        pipe = Pipeline([
            ('log_scaler', LogTransformer()),
            ('clf', self.cfg.model)
        ])
        self.gs = GridSearchCV(
            estimator=pipe,
            param_grid=OmegaConf.to_container(self.cfg.search_space, resolve=True),
            scoring='accuracy', 
            cv=5, 
            n_jobs=-1, 
            verbose=1
        )
        
    def load_data(self):
        logger.info('Load data...')
        if os.path.isfile(self.cfg.data_params['raw_data_path']):
            df = pd.read_csv(self.cfg.data_params['raw_data_path'])
            return df
        return None

    def split_data(self, df):
        logger.info('Split data...')
        df_train, df_oos = train_test_split(
            df, 
            stratify=df['condition'], 
            test_size=self.cfg.data_params['test_size'], 
            random_state=self.RS
        )
        df_train.to_csv(self.cfg.data_params['train_data_path'], index=False)
        df_oos.to_csv(self.cfg.data_params['test_data_path'], index=False)
        X_train, y_train = df_train.drop(columns=['condition']), df_train['condition']
        X_test, y_test = df_oos.drop(columns=['condition']), df_oos['condition']
        return X_train, y_train, X_test, y_test
    
    def fit(self, X_train, y_train):
        logger.info("Training starts...")
        t0 = time()
        self.gs.fit(X_train, y_train)
        logger.info("done in %0.3fs" % (time() - t0))
        logger.info("Best params are : %s" % self.gs.best_params_)
        logger.info('Best training accuracy: %.3f' %self.gs.best_score_)
        
    def predict(self, X_test):
        return self.gs.best_estimator_.predict(X_test)
    
    def validate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        metric = accuracy_score(y_test, y_pred)
        with open(self.cfg.metrics_path, "w") as f:
            json.dump({"accuracy_score": metric}, f)
        logger.info('Test set accuracy score for best params: %.3f ' % metric)
        
    def save_model(self):
        pickle.dump(self.gs.best_estimator_, open(self.cfg.model_path, 'wb'))
        logger.info('Fitted model saved: %s' % self.cfg.model_path)
