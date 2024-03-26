FROM python:3.10-slim

RUN groupadd -r appuser && useradd -r -g appuser appuser
WORKDIR /app
RUN chown -R appuser:appuser /app


RUN pip install --upgrade pip
RUN pip install poetry


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml /app/
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-interaction --no-ansi
RUN pip uninstall --yes poetry


USER appuser

COPY ./phishtank/ /app/
