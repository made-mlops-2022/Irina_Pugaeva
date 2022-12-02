import sys
import json
import logging
import pathlib
import joblib
import pandas as pd
from typing import Union

from fastapi import FastAPI
from fastapi_health import health
from pydantic import BaseModel

# TO do импортировать предиктор, а не модель
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

app = FastAPI(
    title="Heart disease Model API",
    description="A simple API that use classificator to predict heart diseases",
    version="0.1",
)

# load model
model_path = pathlib.Path(".") / "ml_project" / "models" / "clf_pipeline.pickle"
print(model_path)

# with open(model_path, "rb") as f:
#     model = joblib.load(f)
model = None


@app.on_event("startup")
def load_model():
    """Load model"""
    logger.info("Загрузка модели...")
    model_path = pathlib.Path(".") / "ml_project" / "models" / "clf_pipeline.pickle"
    with open(model_path, "rb") as f:
        global model
        model = joblib.load(f)


@app.get("/")
async def root():
    """Root app message"""
    return {"Heart disease classificator"}


@app.get("/predict")
def predict(data_json: str):
    """A simple function that predict heart disease"""
    logger.info("Загрузка данных...")
    data = json.loads(data_json)  # dict = {"col1": 123123, } # list
    data = pd.DataFrame.from_records([data])
    # perform prediction
    print(data)
    logger.info("Предсказание классов...")
    prediction = model.predict(data).item(0)  # array

    # output dictionary
    is_disease = {0: "Negative", 1: "Positive"}

    # show results
    result = {"prediction": is_disease[prediction]}

    # return result
    return result


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}


def check_health():
    return model is not None


app.add_api_route("/health", health([check_health]))
