import pathlib

import click
from hdc.predictor import Predictor

default_cfg_path = pathlib.Path(".") / "configs" / "predict.json"


@click.command(name="predict")
@click.argument("cfg_path", default=default_cfg_path)
def predict_command(cfg_path: str):
    predictor = Predictor(cfg_path)
    data = predictor.load_data()
    predictions = predictor.predict(data)
    predictor.predictions_to_excel(predictions, data)


if __name__ == "__main__":
    predict_command()
