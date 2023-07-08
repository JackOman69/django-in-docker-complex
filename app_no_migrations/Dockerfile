FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE fitness.settings
ENV ROOT_DIR /usr/src
ARG WM_VERSION=v2021.03.01.00

RUN apt-get update \
    && apt-get install -y \
    build-essential git curl unzip \
    python3-dev gcc \
    gfortran libffi-dev \
    libssl-dev libxml2-dev \
    libxslt-dev libjpeg-dev \
    zlib1g-dev libpq-dev \
    libcairo2-dev pkg-config
    
RUN curl -L https://github.com/facebook/watchman/releases/download/$WM_VERSION/watchman-$WM_VERSION-linux.zip -o watchman-$WM_VERSION-linux.zip && \ 
    unzip watchman-$WM_VERSION-linux.zip && \ 
    cd watchman-$WM_VERSION-linux && \ 
    mkdir -p /usr/local/{bin,lib} /usr/local/var/run/watchman && \ 
    cp bin/* /usr/local/bin && \ 
    cp lib/* /usr/local/lib && \ 
    chmod 755 /usr/local/bin/watchman && \ 
    chmod 2777 /usr/local/var/run/watchman && \ 
    cd .. && \ 
    rm -fr watchman-$WM_VERSION-linux.zip watchman-$WM_VERSION-linux 

WORKDIR $ROOT_DIR

COPY . $ROOT_DIR

RUN pip install --upgrade cython \ 
    && pip install --no-cache-dir --upgrade pip \ 
    && pip install -r $ROOT_DIR/requirements.txt --no-cache-dir \
    && chmod 777 -R $ROOT_DIR \
    && chown -R www-data:www-data $ROOT_DIR 

USER www-data 
