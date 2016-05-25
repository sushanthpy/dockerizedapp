"""
Models for the mobile app.
"""
from django.db import models


class Mobile(models.Model):
    """A mobile."""
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()