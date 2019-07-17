Instructions
============

Development Environment Setup
-----------------------------

1. Install dependencies::

    pip3 install pipenv
    pipenv install --dev

2. Start PostgreSQL server::

    docker-compose -f tools/local.yml up -d

3. Activate virtual environment::

    pipenv shell

4. Run migrations::

    cd dev/
    python manage.py makemigrations
    python manage.py migrate

5. Create superuser::

    python manage.py createsuperuser

6. Run server::

    python manage.py runserver

