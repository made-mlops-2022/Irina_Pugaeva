import os
import pickle
import click

import pandas as pd
from sklearn.preprocessing import StandardScaler

DATA_PATH = "data.csv"
TARGET_PATH = "target.csv"
PROCESSED_DATA_PATH = "preprocessed_data.csv"


@click.command("preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
def preprocess_data(input_dir: str, output_dir: str):
    data = pd.read_csv(os.path.join(input_dir, DATA_PATH), index_col=0)
    target = pd.read_csv(os.path.join(input_dir, TARGET_PATH), index_col=0)
    cols = data.columns
    
    sc = StandardScaler()
    preprocessed_data = sc.fit_transform(data)
    preprocessed_data = pd.DataFrame(data=preprocessed_data, columns=cols)
    
    os.makedirs(output_dir, exist_ok=True)
    preprocessed_data.to_csv(os.path.join(output_dir, PROCESSED_DATA_PATH), index=False)
    target.to_csv(os.path.join(output_dir, TARGET_PATH), index=False)


if __name__ == "__main__":
    preprocess_data()
