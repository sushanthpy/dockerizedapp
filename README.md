
Django project called MDB, the Mobile Database, 
which is a database of mobiles exposed through a REST API.

The API is currently able to create, delete and list mobiles using JSON representations.

## Test results
![alt tag](https://travis-ci.org/chanduch06/mdb.svg?branch=master)

## Setup
<br />
To install the dependencies, run: <br />
    python setup.py install
<br />
Then, create the sqlite database and load sample data: <br />
    python manage.py makemigrations <br />
    python manage.py migrate  <br />
    python manage.py loaddata sample_mobiles <br />

Running tests: <br />
    python manage.py test

