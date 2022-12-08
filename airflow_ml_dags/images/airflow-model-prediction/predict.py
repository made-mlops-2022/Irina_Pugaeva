import os
import pickle

import click
import pandas as pd


DATA_PATH = "data_scaled.csv"
MODEL_PATH = "model.pkl"
PREDS_PATH = "predictions.csv"


@click.command()
@click.option("--input_dir")
@click.option("--model_dir")
@click.option("--preds_dir")
def predict(input_dir: str, model_dir: str, preds_dir: str) -> None:
    path = os.path.join(input_dir, DATA_PATH)
    data = pd.read_csv(path)

    model_path = os.path.join(model_dir, MODEL_PATH)
    with open(model_path, 'rb') as fin:
        model = pickle.load(fin)
    preds = model.predict(data)

    os.makedirs(preds_dir, exist_ok=True)
    pred = pd.DataFrame(preds)
    pred_path = os.path.join(preds_dir, PREDS_PATH)
    pred.to_csv(pred_path, index=False)


if __name__ == '__main__':
    predict()