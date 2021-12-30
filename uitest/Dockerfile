FROM python:3.7.5-slim
  
ENV PYTHONIOENCODING utf-8
WORKDIR /test

RUN mkdir /images

RUN apk add --update
RUN apk add libffi-dev
RUN apk add --update py-pip
RUN apk add build-base

RUN apk add --update \
        wget \
    # Add chromium and dependences
        udev \
        chromium \
        chromium-chromedriver \
    # Add selenium
    && pip install selenium \
    && pip install requests \
    && pip install pytest

ENV WEB_HOST 127.0.0.1
ENV WEB_PORT 80

