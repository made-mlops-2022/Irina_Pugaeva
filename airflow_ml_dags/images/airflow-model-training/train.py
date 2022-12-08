import os
import click
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression

TRAIN_DATA_PATH = "train_data.csv"
TRAIN_TARGET_PATH = "train_target.csv"
MODEL_PATH = 'model.pkl'
RANDOM_STATE = 42


@click.command("train")
@click.option("--input-dir")
@click.option("--output-dir")
def train(input_dir: str, output_dir: str):

    data = pd.read_csv(os.path.join(input_dir, TRAIN_DATA_PATH))
    targets = pd.read_csv(os.path.join(input_dir, TRAIN_TARGET_PATH))

    clf = LogisticRegression(random_state=RANDOM_STATE)
    clf.fit(X_train, y_train)

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, MODEL_PATH), "wb") as f:
        pickle.dump(clf, f)


if __name__ == "__main__":
    train()
