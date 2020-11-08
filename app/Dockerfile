# pull official base image
FROM python:3.8.3-slim

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

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

##RUN DJANGO_MODE=build django-admin makemessages --all
##RUN DJANGO_MODE=build django-admin compilemessages
