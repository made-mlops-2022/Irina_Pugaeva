import os
import pickle
import json
import click

import pandas as pd
from sklearn.metrics import f1_score

VAL_DATA_PATH = "val_data.csv"
VAL_TARGET_PATH = "val_target.csv"

MODEL_PATH = "model.pkl"
METRIC_PATH = "metrics.txt"


@click.command("validate")
@click.option("--input-dir")
@click.option("--model-dir")
def validate(input_dir: str, model_dir: str):

    X_val = pd.read_csv(os.path.join(input_dir, VAL_DATA_PATH))
    y_val = pd.read_csv(os.path.join(input_dir, VAL_TARGET_PATH))

    with open(os.path.join(model_dir, MODEL_PATH), "rb") as f:
        model = pickle.load(f)
    preds = model.predict(X_val)
    f1_score_value = f1_score(y_val, preds, average="macro")

    with open(os.path.join(model_dir, METRIC_PATH), "w") as f:
        f.write("f1_score {}".format(f1_score_value))


if __name__ == "__main__":
    validate()
