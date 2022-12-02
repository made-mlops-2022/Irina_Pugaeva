Запуск из корня проекта (Irina_Pugaeva):

uvicorn online_inference.app.main:app --reload


Запуск через докер:

docker build -t app .
docker run -it -p 8000:8000 app