from setuptools import setup

setup(
    name='MDB',
    description='Mobile DataBase',
    version='0.0.1',
    packages=['mdb', 'mobiles'],
    install_requires=[
        'django==1.9.5',
        'simplejson',
        'nose',
        'mock',
    ]
)
