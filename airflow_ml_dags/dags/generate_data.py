import os
from datetime import timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount


DEFAULT_ARGS = {
    "owner": "Pugaeva Irina",
    "email": ["pugaevaarina@gmail.com"],
    "email_on_failure": True,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "max_active_runs": 1,
}

DATA_DIR = "data/raw"
MOUNT = Mount(
    source="/Users/alexandersidorenko/ira/mlops/Irina_Pugaeva/airflow_ml_dags/data/",
    target="/data",
    type="bind",
)

with DAG(
    "data_generator",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",
    start_date=days_ago(10),
) as dag:

    path = os.path.join("/", DATA_DIR, "{{ ds }}")
    generate_data = DockerOperator(
        task_id="get_data",
        image="airflow-data-generation",
        command=f"--output-dir={path}",
        network_mode="bridge",
        do_xcom_push=False,
        mounts=[MOUNT],
    )

    generate_data
