# Докеризация API для Ya|MDb. Интернет-сервис о кино на базе Django REST

![Build Status](https://github.com/vostavhy/yamdb_final/workflows/yamdb_final/badge.svg)

## Установка

#### Шаг первый. Установка Docker и docker-compose
Для установки воспользуйтесь официальной [инструкцией](https://docs.docker.com/engine/install/).

#### Шаг второй. Создание переменных окружения
В папке api_yamdb создайте файл .env и пропишите в нём следущие переменные окружения
```bash
DB_NAME=postgres_db_name
DB_USER=postgres_db_user
DB_PASSWORD=postgres_db_password
DB_HOST=db
DB_PORT=5432
```
#### Шаг третий. Сборка и запуск контейнера
```bash
docker-compose up -d --build
```
#### Шаг четвертый. База данных
```bash
docker-compose run web python manage.py makemigrations --no-input
docker-compose run web python manage.py migrate --no-input
```
#### Шаг пятый. Сбор статики
```bash
docker-compose run web python manage.py collectstatic --no-input
```
## Использование
### Создание суперпользователя Django
```bash
docker-compose run web python manage.py createsuperuser
```
### Импорт данных в формате .json
```bash
docker-compose run web python manage.py loaddata path/to/your/json
```
##### Пример инициализации стартовых данных:
```bash
docker-compose run web python manage.py loaddata fixtures.json
```
### Выключение контейнера
```bash
docker-compose down
```
