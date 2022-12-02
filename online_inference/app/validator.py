from typing import Literal
from pydantic import BaseModel, validator
from fastapi.exceptions import HTTPException


class ResponseData(BaseModel):
    condition: Literal[0, 1]


class RequestData(BaseModel):
    age: float
    sex: Literal[0, 1]
    cp: Literal[0, 1, 2, 3]
    trestbps: float
    chol: float
    fbs: Literal[0, 1]
    restecg: Literal[0, 1, 2]
    thalach: float
    exang: Literal[0, 1]
    oldpeak: float
    slope: Literal[0, 1, 2]
    ca: Literal[0, 1, 2, 3]
    thal: Literal[0, 1, 2]

    @validator("age")
    def validate_age(cls, val):
        if val < 0 or val > 100:
            raise HTTPException(status_code=400, detail="Wrong age"])
        return val

    @validator("chol")
    def validation_chol(cls, val):
        if val < 0 or val > 500:
            raise HTTPException(status_code=400, detail="Wrong chol")
        return val
