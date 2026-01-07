# ===================
# Docker Commands
# ===================
up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

# ===================
# Django Commands
# ===================
django-run:
	cd apps/django-api && python manage.py runserver

django-migrate:
	cd apps/django-api && python manage.py migrate

django-makemigrations:
	cd apps/django-api && python manage.py makemigrations

django-shell:
	cd apps/django-api && python manage.py shell

django-superuser:
	cd apps/django-api && python manage.py createsuperuser

# ===================
# FastAPI Commands
# ===================
fastapi-run:
	cd apps/fastapi-realtime && uvicorn app.main:app --reload --port 8001

# ===================
# Frontend Commands
# ===================
frontend-dev:
	cd apps/web && npm run dev

frontend-build:
	cd apps/web && npm run build

frontend-install:
	cd apps/web && npm install

# ===================
# Celery Commands
# ===================
celery-worker:
	cd apps/django-api && celery -A config worker --loglevel=info

celery-beat:
	cd apps/django-api && celery -A config beat --loglevel=info