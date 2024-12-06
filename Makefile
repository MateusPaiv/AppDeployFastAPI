run-production:
	alembic upgrade head && gunicorn --worker-tmp-dir /dev/shm --config gunicorn.config.py app.main:app

run-dev:
	alembic upgrade head && uvicorn app.main:app

create-db-migration:
	@echo "Migration title: "; \
	read title; \
	alembic revision -m "$$title"