.PHONY: backup backups bash build check clean clean-pyc clear-db debug deps down migrate migrations mypy push restore shell show-urls test test-app up up-d

backup:
				docker compose run --rm postgres backup

backups:
				docker compose run --rm postgres backups

bash:
				docker compose run --rm django /bin/bash

build:
				docker compose build

check:
				pre-commit run --all-files

clean:  clean-pyc
				docker compose down -v --remove-orphans
				docker compose down -v --remove-orphans

clean-pyc:
				sudo find . -name '*.pyc' -exec rm {} +
				sudo find . -name '*.pyo' -exec rm {} +
				sudo find . -name '*~' -exec rm {} +
				sudo find . -name '__pycache__' -exec rm -fr {} +
				sudo rm -fr src/.ipython

clear-db:
				docker compose run --rm django python manage.py flush


deps: down
				docker compose up -d postgres mailhog

down:
				docker compose down --remove-orphans
				docker compose down --remove-orphans

migrate:
				docker compose run --rm django python manage.py migrate

migrations:
				docker compose run --rm django python manage.py makemigrations --name $(name)

mypy:
				docker compose run --rm django mypy anvara_assessment

restore:
				docker compose run --rm postgres restore $(file)

shell:
				docker compose run --rm django python manage.py shell

test:
				docker compose run --rm django pytest

test-app:
				docker compose run --rm django pytest $(app)

up: down
				docker compose up
