import pathlib

from hdc.trainer import Trainer


if __name__ == '__main__':
    cfg_path = pathlib.Path(".") / "configs" / "train_svm.json"
    trainer = Trainer(cfg_path)
    X_train, y_train, X_test, y_test = trainer.load_data()
    trainer.fit(X_train, y_train)
    trainer.validate(X_test, y_test)
    trainer.save_model()
