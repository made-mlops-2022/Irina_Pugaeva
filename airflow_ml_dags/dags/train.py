from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from airflow.utils.dates import days_ago


DEFAULT_ARGS = {
    "owner": "Pugaeva Irina",
    "email": ["pugaevaarina@gmail.com"],
    "email_on_failure": True,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "max_active_runs": 1,
}

RAW_DATA_PATH = "/data/raw/{{ ds }}"
PROCESSED_DATA_PATH = "/data/processed/{{ ds }}"
SPLITTED_DATA_PATH = "/data/splitted/{{ ds }}"
MODEL_PATH = "/data/models/lr/{{ ds }}"
MOUNT = Mount(
    source="/Users/alexandersidorenko/ira/mlops/Irina_Pugaeva/airflow_ml_dags/data/",
    target="/data",
    type="bind",
)
SENSOR_ARGS = {"poke_interval": 10, "timeout": 60, "mode": "reschedule"}


with DAG(
    "train",
    default_args=DEFAULT_ARGS,
    schedule_interval="@weekly",
    start_date=days_ago(10),#pendulum.today("UTC").add(days=0),
) as dag:

    preprocess_data = DockerOperator(
        task_id="data-preprocessing",
        image="airflow-data-preprocessing",
        command=f"--input-dir={RAW_DATA_PATH} --output-dir={PROCESSED_DATA_PATH}",
        network_mode="bridge",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[MOUNT],
    )

    split_data = DockerOperator(
        task_id="data-splitting",
        image="airflow-data-splitting",
        command=f"--input-dir={PROCESSED_DATA_PATH} --output-dir={SPLITTED_DATA_PATH}",
        network_mode="bridge",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[MOUNT],
    )

    train_model = DockerOperator(
        task_id="model-training",
        image="airflow-model-training",
        command=f"--input-dir={SPLITTED_DATA_PATH} --output-dir={MODEL_PATH}",
        network_mode="bridge",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[MOUNT],
    )

    val_model = DockerOperator(
        task_id="validation",
        image="airflow-model-validation",
        command=f"--model-dir={MODEL_PATH} --data-dir={PROCESSED_DATA_PATH}",
        network_mode="bridge",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[MOUNT],
    )

    preprocess_data >> split_data >> train_model >> val_model
