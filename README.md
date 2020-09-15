# Докеризация API для Ya|MDb. Интернет-сервис о кино на базе Django REST

![Build Status](https://github.com/vostavhy/yamdb_final/workflows/yamdb_final/badge.svg)

## Установка

#### Шаг первый. Проверьте установлен ли у вас Docker и docker-compose

```bash
docker -v
```
Если у вас все еще не установлен Docker и вы используете Linux, то воспользуйтесь скриптом:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh # эта команда запустит его
```
Если же у вас другая ОС, то воспользуйтесь официальной [инструкцией](https://docs.docker.com/engine/install/).

Далее также проверяем наличие docker-compose:
```bash
docker-compose -v
```
Если у вас не установлен docker-compose и вы пользователь системы Linux, то вы можете установить его из официального репозитория:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
#Как только завершилась установка, измените права доступа права доступа
sudo chmod +x /usr/local/bin/docker-compose
```
Данная инструкция взята из [документации Docker](https://docs.docker.com/engine/install/). Там же вы найдете инструкцию по установке docker-compose на другие системы.

#### Шаг второй. Сборка контейнера
```bash
docker-compose build
```
#### Шаг третий. Запуск контейнера
```bash
docker-compose up
```
#### Шаг четвертый. База данных
```bash
docker-compose run web python manage.py migrate --no-input
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