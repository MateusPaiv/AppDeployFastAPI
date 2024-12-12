run-production:
	cd src && alembic upgrade head && cd .. && gunicorn --worker-tmp-dir /dev/shm --config gunicorn.config.py src.app.main:app

run-dev:
	cd src && alembic upgrade head && cd .. && uvicorn src.app.main:app

create-db-migration:
	@echo "Migration title: "; \
	read title; \
	alembic revision -m "$$title"