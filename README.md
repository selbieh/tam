# Phonebook

A Django phonebook application to manage contacts and their phone numbers.

## Database Schema

The database consists of two tables: `Contact` and `PhoneNumber`.

### Contact Table

| Column | Type        | Description             |
| ------ | ----------- | ----------------------- |
| id     | integer     | Primary key for contact |
| name   | varchar(50) | Name of the contact     |

### PhoneNumber Table

| Column     | Type        | Description                                       |
| ---------- | ----------- | ------------------------------------------------- |
| id         | integer     | Primary key for phone number                      |
| contact_id | integer     | Foreign key to `Contact` table (one-to-many link) |
| number     | varchar(20) | Phone number for the contact                      |

The `contact_id` column in the `PhoneNumber` table establishes a one-to-many relationship between the `Contact` and `PhoneNumber` tables, allowing a single contact to have multiple phone numbers.

## Running the Application

1. **Build the Docker stack**:
   ```sh
   docker-compose -f local.yml build
   ```
   Ensure pre-commit is installed globally on your local machine.

2. **Run the stack**:
   ```sh
   docker-compose -f local.yml up
   ```
   Alternatively, use:
   ```sh
   docker-compose up
   ```
   if you have set the `COMPOSE_FILE` environment variable to `local.yml`.

3. **Execute management commands**:
   ```sh
   docker-compose -f local.yml run --rm django python manage.py [command]
   ```

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Settings are moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- **Create a normal user account**: Go to Sign Up, fill out the form, and submit. Verify your email using the simulated email verification message in your console.

- **Create a superuser account**:
   ```sh
   python manage.py createsuperuser
   ```

For convenience, keep your normal user logged in on one browser and your superuser logged in on another to see the site behavior for both types of users.

### Type Checks

Run type checks with mypy:
```sh
mypy phonebook
```

### Test Coverage

To run tests, check coverage, and generate an HTML report:
```sh
coverage run -m pytest
coverage html
open htmlcov/index.html
```

#### Running tests with pytest

```sh
pytest
```

### Live Reloading and Sass CSS Compilation

Details moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

For deployment details, refer to the [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
