# Anvara Assessment

Backend developer assessment for anvara

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Basic Commands

### Setting Up Your Environment

- The project is fully dockerized, so you need to have docker and docker-compose installed on your machine:
The following command will build the docker images and run the containers:

      $ make up

### Documentation
You can view the Swagger API documentation at `http://127.0.0.1:8000/api/docs/`

### Setting Up Your Users

- To create a **superuser account**, use this command:

      $ make bash
      $ python manage.py createsuperuser

#### Running tests with pytest

    $ make test

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`
