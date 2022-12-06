FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --dev --system --deploy
