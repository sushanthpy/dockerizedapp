
Django project called MDB, the Mobile Database, 
which is a database of mobiles specs exposed through a REST API.

The API is currently able to create, delete and list mobiles using JSON representations.

## Image Status
[![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=sushanthpy&repoName=dockerizedapp&branch=master&pipelineName=dockerizedapp&accountName=sushanth&type=cf-1)]( https://g.codefresh.io/repositories/sushanthpy/dockerizedapp/builds?filter=trigger:build;branch:master;service:58cfd0cc5447520100556318~dockerizedapp)

## Test results
![alt tag](https://travis-ci.org/sushanthpy/dockerizedapp.svg?branch=master)

## Code Quality
[![Code Health](https://landscape.io/github/sushanthpy/dockerizedapp/master/landscape.svg?style=flat)](https://landscape.io/github/sushanthpy/dockerizedapp/master)

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

