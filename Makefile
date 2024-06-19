ifeq ($(wildcard /code),)
PYTHON=PYTHONPATH=$$PYTHONPATH:../.. python3
else
PYTHON=python3
endif

MANAGE_PY=$(PYTHON) manage.py

.PHONY:
migrate:
	$(MANAGE_PY) migrate

.PHONY:
runserver:
	$(MANAGE_PY) runserver 0.0.0.0:8000


.PHONY:
celery_worker:
	celery -A l2pay worker --loglevel=info


.PHONY:
celery_beat:
	celery -A l2pay beat --loglevel=info