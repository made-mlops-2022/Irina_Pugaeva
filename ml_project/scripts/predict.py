import pathlib

from hdc.predictor import Predictor


if __name__ == '__main__':
    cfg_path = pathlib.Path(".") / "configs" / "predict.json"
    predictor = Predictor(cfg_path)
    data = predictor.load_data()
    predictions = predictor.predict(data)
    predictor.predictions_to_excel(predictions, data)
