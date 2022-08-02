pip3 install -r requirements.txt;
pre-commit install;
docker-compose up;
docker exec -it airflow-container bash;