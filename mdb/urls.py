"""
URLs for the mdb project.
"""
from django.conf.urls import patterns, include, url

patterns('', url(r'^mobiles/', include('mobiles.urls')))
