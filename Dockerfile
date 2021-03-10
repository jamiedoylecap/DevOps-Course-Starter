FROM python:3.8-buster as base
WORKDIR /
COPY pyproject.toml .
RUN pip install poetry && poetry install --no-root && poetry add gunicorn && poetry add pytest
EXPOSE 5000

# production
FROM base as prod
COPY . .
ENTRYPOINT ["poetry","run","gunicorn","-w","4","-b","0.0.0.0","todoapp.app:create_app()"]

# development
FROM base as dev
ENTRYPOINT ["poetry","run","flask","run","--host=0.0.0.0"]

# testing
FROM base as test
ENTRYPOINT ["poetry","run","pytest"]
