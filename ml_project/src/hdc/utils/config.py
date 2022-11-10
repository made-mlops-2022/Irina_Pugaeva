from dataclasses import dataclass
from dataclasses_json import dataclass_json

from typing import Dict, List, Any


@dataclass_json
@dataclass
class TrainConfig:
    model: Dict[str, Any]
    model_path: str
    metrics_path: str
    search_space: Dict[str, Any]
    data_params: Dict[str, Any]


@dataclass_json
@dataclass
class PredictConfig:
    model_path: str
    data_params: Dict[str, Any]
