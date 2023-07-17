FROM python:3.9.6-alpine
LABEL maintainer="mail@hidonash.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app
WORKDIR /usr/src/app

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]

EXPOSE 5000
