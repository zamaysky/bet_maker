## Зависимости

Для запуска проекта на сервере необходимо установить [docker](https://docs.docker.com/engine/install/ubuntu/)

## Список сервисов

- Python 3.11.8 + FastAPI
- PostgreSQL 15.4

Запустить проект:

```bash
docker compose up --detach --build
```

Документация:
```
http://localhost:8000/docs
```

Запуск тестов
```bash
docker exec -it bet_maker_backend poetry run pytest
```
