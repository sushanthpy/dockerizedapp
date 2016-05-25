"""
URLs for the cars app.
"""
from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$',  views.MobileView.as_view(), name='mobiles'),
)
