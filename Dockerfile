FROM python:3.10-alpine

WORKDIR /app
COPY . /app

RUN python3.10 -m pip --no-cache-dir install --upgrade pip
RUN pip install --no-cache-dir poetry
RUN poetry install --no-root --no-cache