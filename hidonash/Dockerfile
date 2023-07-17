FROM python:3.11
LABEL maintainer="mail@hidonash.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

COPY . /code/
WORKDIR /code/

ENTRYPOINT ["./entrypoint.sh"]

RUN useradd wagtail
RUN chown -R wagtail /code

EXPOSE 8000

USER wagtail
