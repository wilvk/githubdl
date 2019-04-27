FROM python:3.7-alpine3.7

RUN apk update

RUN apk add build-base
RUN apk add libffi-dev
RUN apk add libressl-dev

RUN pip install --upgrade pip

RUN pip install pyyaml
RUN pip install twine
RUN pip install requests
RUN pip install nose
RUN pip install wheel
