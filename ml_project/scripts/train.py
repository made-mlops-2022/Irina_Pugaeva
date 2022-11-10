import pathlib

import click
from hdc.trainer import Trainer

default_cfg_path = pathlib.Path(".") / "configs" / "train_svm_033.json"

@click.command(name="fit")
@click.argument("cfg_path", default=default_cfg_path)
def fit_command(cfg_path: str):
    trainer = Trainer(cfg_path)
    df = trainer.load_data()
    X_train, y_train, X_test, y_test = trainer.split_data(df)
    trainer.fit(X_train, y_train)
    trainer.validate(X_test, y_test)
    trainer.save_model()

if __name__ == '__main__':
    fit_command()
