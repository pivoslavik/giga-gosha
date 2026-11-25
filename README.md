# giga-gosha
bot for applying to job openings

## Локальный запуск

Перед первым запуском скопируйте пример настроек и при необходимости измените значения в `.env`.

```sh
cp .env.example .env
docker compose up -d --build --wait
```

В `.env` задаются параметры подключения к PostgreSQL и Kafka, имя топика и идентификатор кластера. Конфигурация одного локального брокера хранится в `infra/kafka/server.properties`.

## Разработка

В `services/` находятся четыре сервиса на Python 3.12.16: `bot`, `parser`, `ml` и `integration`. Каждый запускается из корня командой вида `python -m services.bot` и отвечает на `GET /health` на порту 8080. Для одновременного запуска используйте Compose.

Чтобы выполнить те же проверки, что и GitHub Actions, установите инструменты в виртуальное окружение:

```sh
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
black --check packages services tests
python -m unittest discover -s tests
```
