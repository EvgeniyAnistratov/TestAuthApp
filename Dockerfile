FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

RUN python3.11 -m pip --no-cache-dir install --upgrade pip
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-cache

EXPOSE 8000

CMD ["poetry", "run", "python3.11", "auth_app/manage.py", "runserver", "0.0.0.0:8000"]