# pull official base image
FROM python:3.8.3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y gettext libgettextpo-dev && apt-get -y clean

RUN apt-get install -y \
        netcat \
        git \
        python3-dev \
        python3-lxml \
        build-essential \
        libffi-dev \
        apt-utils \
    && apt-get -y clean


COPY Pipfile Pipfile.lock /usr/src/app/
RUN pip3 install --upgrade setuptools pip
RUN pip3 install pipenv && pipenv install --system

# copy entrypoint.sh
#COPY ./entrypoint.sh .

# copy project
COPY . /usr/src/app/
#COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

#
## Pull base image
#FROM python:3.8-slim
#
#ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8
#
## Set environment varibles
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## Set work directory
#WORKDIR /Docker
#
## Install dependencies
#COPY Pipfile Pipfile.lock /Docker/
##RUN pip install --upgrade setuptools pip
#RUN pip install pipenv && pipenv install --system
#RUN apt-get update && apt-get install -y gettext libgettextpo-dev && apt-get -y clean
#
##RUN DJANGO_MODE=build django-admin makemessages --all
##RUN DJANGO_MODE=build django-admin compilemessages
#
## Copy project
#COPY . /Docker/
#
