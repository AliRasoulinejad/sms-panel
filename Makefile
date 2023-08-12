all: pre-commit test

pre-commit:
	poetry run pre-commit run --all-files

test:
	./manage.py test --settings=config.django.test

coverage:
	coverage run manage.py test --settings=config.django.test
	coverage html
	@echo check results in below line:
	@echo "file:///$(shell pwd)/htmlcov/index.html"

run:
	./manage.py runserver

# -----------------------------------------------------------------------
build:
	sudo docker build . -f ./docker/Dockerfile.local

compose-prepare:
	sudo cp .env.example .compose/.env

compose-up:
	sudo docker compose up --build

compose-down:
	sudo docker compose down --remove-orphans

# -----------------------------------------------------------------------
