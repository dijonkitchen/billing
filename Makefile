install:
	poetry install

server:
	docker compose up -d
	poetry run uvicorn billing.main:app --reload

teardown:
	docker compose down

test:
	poetry run pytest -vv
