import os
import click

import pandas as pd
from sklearn.model_selection import train_test_split

PROCESSED_DATA_PATH = "preprocessed_data.csv"
TARGET_PATH = "target.csv"

TRAIN_DATA_PATH = "train_data.csv"
TRAIN_TARGET_PATH = "train_target.csv"

VAL_DATA_PATH = "val_data.csv"
VAL_TARGET_PATH = "val_target.csv"

TEST_SIZE = 0.33
RANDOM_STATE = 42


@click.command("split")
@click.option("--input-dir")
@click.option("--output-dir")
def split(input_dir: str, output_dir: str):
    data = pd.read_csv(os.path.join(input_dir, PROCESSED_DATA_PATH))
    target = pd.read_csv(os.path.join(input_dir, TARGET_PATH))

    X_train, X_val, y_train, y_val = train_test_split(
        data, target, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    os.makedirs(output_dir, exist_ok=True)

    X_train.to_csv(os.path.join(output_dir, TRAIN_DATA_PATH), index=False)
    y_train.to_csv(os.path.join(output_dir, TRAIN_TARGET_PATH), index=False)
    X_val.to_csv(os.path.join(output_dir, VAL_DATA_PATH), index=False)
    y_val.to_csv(os.path.join(output_dir, VAL_TARGET_PATH), index=False)


if __name__ == "__main__":
    split()
