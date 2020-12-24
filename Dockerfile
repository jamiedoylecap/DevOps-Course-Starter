FROM python:3.8-buster
WORKDIR /todo
COPY pyproject.toml .
RUN pip install poetry && poetry install --no-root && pip install gunicorn

EXPOSE 5000

ENTRYPOINT ["poetry","run","flask","run","--host=0.0.0.0"]