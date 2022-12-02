import sys
import json
import logging
import pandas as pd
import pathlib
import requests

PATH_TO_DATA = (
    pathlib.Path(".") / "ml_project" / "data" / "scoring_data" / "scoring_data.csv"
)
LOCALHOST = "127.0.0.1"
PORT = 8000
DOMAIN = f"{LOCALHOST}:{PORT}"
ENDPOINT = "predict"

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

data = pd.read_csv(PATH_TO_DATA).head() # первые пять сэмплов
# data.drop(data.filter(regex="Unname"),axis=1, inplace=True)
print(data)
data = data.drop("condition", axis=1)
data_requests = data.to_dict(orient="records")

for request in data_requests:
    print()
    print(json.dumps(request))
    response = requests.post(f"http://{DOMAIN}/{ENDPOINT}", json=request)

    logger.info("Sending request...")
    logger.info(f"Response status_code: {response.status_code}")
    logger.info(f"Response prediction: {response.json()}")
