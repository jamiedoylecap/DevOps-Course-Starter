FROM python:3.8-buster as base
WORKDIR /
COPY pyproject.toml .
RUN pip install poetry && poetry install --no-root && poetry add gunicorn
EXPOSE 5000
ENTRYPOINT ["poetry","run","gunicorn","-w","4","-b","0.0.0.0","todo-app/app"]

FROM base as prod
COPY . .

FROM base as dev
# Nothing needed