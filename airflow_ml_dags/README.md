### Для корректной работы с переменными, созданными из UI

    export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")


### Запуск airflow:

    docker compose up --build

### http://127.0.0.1:8080


### Остановка airflow

    docker compose down

### Запуск тестирования

    pytest tests