# python3.9のイメージをダウンロード
FROM python:3.11.2
ENV PYTHONUNBUFFERED=1

WORKDIR /tmp
RUN pip install poetry
COPY ./FastAPI/src/pyproject.toml* poetry.lock* ./
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

WORKDIR /src

# uvicornのサーバーを立ち上げる
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
