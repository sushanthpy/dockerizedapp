# dockerizedapp

![alt text](https://travis-ci.org/sushanthpy/dockerizedapp.svg "Test cases for cars")


This evaluation consists of a Django project called ICDB, the Internet Car
Database, which is a database of cars exposed through a REST API.

The API is currently able to create and list cars using JSON representations.

## Setup

# To install the dependencies, run:
    python setup.py install

# sqlite database and load sample data:
    python manage.py syncdb
    python manage.py loaddata sample_cars

# Running tests:
    python manage.py test

