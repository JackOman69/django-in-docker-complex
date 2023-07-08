FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE fitness.settings
ENV ROOT_DIR /usr/src

WORKDIR $ROOT_DIR

COPY . $ROOT_DIR

RUN set -ex \
    && apk update --no-cache \  
    && apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps \
    && pip install --no-cache-dir --upgrade pip \
    && pip install -r $ROOT_DIR/requirements.txt --no-cache-dir \
    && apk del .build-deps

RUN apk add postgresql-libs libpq --no-cache
