## Зависимости

Для запуска проекта на сервере необходимо установить [docker](https://docs.docker.com/engine/install/ubuntu/)

## Список сервисов

- Python 3.12 + FastAPI
- PostgreSQL 15

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
docker exec -it bet_maker_backend pytest
```
