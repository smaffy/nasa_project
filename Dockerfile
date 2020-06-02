# Pull base image
FROM python:3.8-slim

ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /Docker

# Install dependencies
COPY Pipfile Pipfile.lock /Docker/
RUN apt-get update && apt-get install -y gettext libgettextpo-dev
RUN pip3 install pipenv && pipenv install --system

#RUN DJANGO_MODE=build django-admin makemessages --all
#RUN DJANGO_MODE=build django-admin compilemessages

# Copy project
COPY . /Docker/


