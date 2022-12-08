import os
import click
from sklearn.datasets import load_breast_cancer


@click.command("generate")
@click.option("--output-dir", required=True)
def get_data(output_dir: str):
    cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    X, y = load_breast_cancer(return_X_y=True, as_frame=True)
    X = X.iloc[:, :13]
    X.columns = cols
    os.makedirs(output_dir, exist_ok=True)
    X.to_csv(os.path.join(output_dir, "data.csv"))
    y.to_csv(os.path.join(output_dir, "target.csv"))

if __name__ == '__main__':
    get_data()