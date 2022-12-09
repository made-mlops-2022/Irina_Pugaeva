from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount


DATA_PATH = "/data/splitted/{{ ds }}"
MODEL_PATH = "/data/model/{{ ds }}"
PREDICTIONS_PATH = "/data/predictions/{{ ds }}"
MOUNT = Mount(
    source="/Users/alexandersidorenko/ira/mlops/Irina_Pugaeva/airflow_ml_dags/data/",
    target="/data",
    type="bind",
)


DEFAULT_ARGS = {
    "owner": "Pugaeva Irina",
    "email": ["pugaevaarina@gmail.com"],
    "email_on_failure": True,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "max_active_runs": 1,
}

with DAG(
    "predict",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",
    start_date=pendulum.today("UTC").add(days=0),
) as dag:
    predict = DockerOperator(
        task_id="docker-airflow-prediction",
        image="airflow-model-prediction",
        command=f"--input-dir={DATA_PATH} --model-dir={MODEL_PATH} --preds-dir={PREDICTIONS_PATH}",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[MOUNT],
    )

    predict
