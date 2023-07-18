FROM python:3.9.6-alpine
LABEL maintainer="mail@hidonash.com"

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY . $APP_HOME

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 8000

ENTRYPOINT ["sh", "/home/app/web/entrypoint.sh"]
