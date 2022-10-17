### Assigment

We would like you to develop a micro service that enables one to create a user, update user information and delete a user. Also create user interface for it using either Angular or React js and Spring boot/python for the backend.

[![codecov](https://codecov.io/gh/foscraft/cloudit-africa-bend/branch/main/graph/badge.svg?token=MPYV7GN93Q)](https://codecov.io/gh/foscraft/cloudit-africa-bend)

### RUNNING THE APPLICATION

#### Prerequisites

`pipenv` should be installed on your machine.

`pip install pipenv` to install pipenv

run `pipenv shell` to activate the virtual environment.

run `pipenv install` to install all the dependencies.

Then run `python manage.py runserver` to start the server.

Swagger UI for local server:  `http://127.0.0.1:8000/api/v1/schema/swagger-ui/`

Swagger UI for production server:  `https://africa-cloudit-demo-bend.herokuapp.com/api/v1/schema/swagger-ui/`

Register a user `http://127.0.0.1:8000/api/v1/users/`

        {
            "email":"tom@hmail.com",
            "username":"tsusth",
            "password":"Distance@205"
        }

Delete a user `http://127.0.0.1:8000/api/v1/users/{lookup_id}/`

Update a user `http://127.0.0.1:8000/api/v1/users/{lookup_id}/`

Login a user `http://127.0.0.1:8000/api/v1/auth/login/`
