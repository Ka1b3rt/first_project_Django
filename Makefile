.PHONY: install test lint run docker-up docker-down

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run ruff check .

run:
	poetry run python src/hotel_booking/manage.py runserver 0.0.0.0:9000

docker-up:
	docker-compose up --build

docker-down:
	docker-compose down