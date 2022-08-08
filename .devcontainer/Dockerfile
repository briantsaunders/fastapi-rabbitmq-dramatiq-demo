# pull official base image
ARG VARIANT="3.9-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# set work directory
WORKDIR /usr/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pip-tools
COPY ./requirements-dev.txt /usr/app/requirements-dev.txt
RUN python3 -m pip install -r requirements-dev.txt --no-cache-dir

# copy project
COPY . /usr/app/
