# Базовый образ с Python
FROM python:3.11-slim

# Установка Poetry
ENV POETRY_VERSION=1.8.2
RUN pip install "poetry==$POETRY_VERSION"

# Рабочая директория
WORKDIR /app

# Копирование файлов Poetry
COPY pyproject.toml poetry.lock* /app/

# Установка зависимостей через Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

# Копирование исходного кода
COPY src/ /app/src/
COPY scripts/ /app/scripts/
COPY tests/ app/tests/

# Установка переменной окружения для Django
ENV PYTHONPATH=/app/src

# Запуск приложения
CMD ["python", "src/hotel_booking/manage.py", "runserver", "0.0.0.0:9000"]