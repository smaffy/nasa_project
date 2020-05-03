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
RUN pip3 install pipenv && pipenv install --system

# Copy project
COPY . /Docker/


