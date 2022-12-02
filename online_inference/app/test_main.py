import json
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

test_request_data = {
    "age": 35,
    "sex": 0,
    "cp": 3,
    "trestbps": 138,
    "chol": 183,
    "fbs": 0,
    "restecg": 0,
    "thalach": 182,
    "exang": 0,
    "oldpeak": 1.4,
    "slope": 0,
    "ca": 0,
    "thal": 0,
}


def test_app_root():
    response = client.get("/")
    assert (
        response.status_code == 200
    ), f"Test_app_root failed with code: {response.status_code}"
    assert "Heart disease classificator" in response.text


def test_app_predict():
    with client:
        response = client.get(json.dumps(test_request_data))
        print(response)
    assert 200 == response.status_code
    # predictions = response.json()
    # assert predictions == {"Condition": "Negative: no disease"}
