FROM python:3.11.2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONUTF8=1

WORKDIR /src

RUN pip install poetry
RUN poetry config virtualenvs.in-project true

COPY ./FastAPI/pyproject.toml ./pyproject.toml
COPY ./FastAPI/poetry.lock ./poetry.lock
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
