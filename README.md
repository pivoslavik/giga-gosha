# giga-gosha
bot for applying to job openings

## Локальный запуск

Перед первым запуском скопируйте пример настроек и при необходимости измените значения в `.env`.

```sh
cp .env.example .env
docker compose up -d --build --wait
```

В `.env` задаются параметры подключения к PostgreSQL и Kafka, имя топика и идентификатор кластера. Конфигурация одного локального брокера хранится в `infra/kafka/server.properties`.
