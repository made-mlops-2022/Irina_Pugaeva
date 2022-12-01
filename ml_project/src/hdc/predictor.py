import json
import pickle

import pandas as pd

from hdc.utils.config import PredictConfig
from hdc.utils.logger import logger


class Predictor:
    def __init__(self, cfg_path) -> None:
        with open(cfg_path) as cfg_file:
            cgf_dict = json.load(cfg_file)
        self.cfg = PredictConfig.from_dict(cgf_dict)
        self.RS = self.cfg.data_params['random_state']
        self.model = pickle.load(open(self.cfg.model_path, 'rb'))
        
    def load_data(self) -> pd.DataFrame:
        data = pd.read_csv(self.cfg.data_params['scoring_data_path'])
        data = data.drop(columns=[self.cfg.data_params["target_col_name"]], errors="ignore")
        return data
        
    def predict(self, data):
        logger.info('Предсказание классов...')
        predictions = self.model.predict(data)
        return predictions

    def predictions_to_excel(self, predictions, data):
        logger.info('Сохранение результатов...')
        data['condition_preds'] = predictions
        data.to_excel(self.cfg.data_params['path_to_result'])
