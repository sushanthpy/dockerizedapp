"""
URLs for the icdb project.
"""
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^mobiles/', include('mobiles.urls')),
)
