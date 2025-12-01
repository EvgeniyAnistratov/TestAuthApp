FROM python:3.10-alpine

WORKDIR /app
COPY . /app

RUN python3.10 -m pip --no-cache-dir install --upgrade pip
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-cache

CMD ["poetry", "run", "python3.10", "auth_app/manage.py", "runserver"]