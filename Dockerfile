# создать образ на основе базового слоя python (там будет ОС и интерпретатор Python)
FROM python:3.8.3-alpine

# обновить ОС, обновить её и установить необходимые библиотеки
RUN apk update\
	&& apk add postgresql postgresql-contrib python3-dev musl-dev\
	&& apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev\
	&& pip install --upgrade pip

# создать папку, скопировать туда всё из текущей папки
RUN mkdir /app
COPY . /app

# создать папку для статики
RUN mkdir /app/static
WORKDIR /app

# установить все зависимости
RUN pip install -r requirements.txt

# run entrypoint.sh
# ENTRYPOINT ["/app/entrypoint.sh"]

# запустить gunicorn
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
