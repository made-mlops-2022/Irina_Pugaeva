FROM python:3.9.4-buster

RUN mkdir /online_inference

RUN mkdir -p /ml_project/models

WORKDIR /

COPY ./online_inference/requirements.txt /app/requirements.txt

COPY ./online_inference/app /online_inference/app

COPY ./ml_project /ml_project

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install ./ml_project

CMD ["uvicorn", "online_inference.app.main:app", "--host", "0.0.0.0", "--port", "8000"]