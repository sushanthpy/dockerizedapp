"""Wsgi file for mdb settings."""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mdb.settings")

from django.core.wsgi import get_wsgi_application

get_wsgi_application()


