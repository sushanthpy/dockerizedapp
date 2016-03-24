"""
URLs for the cars app.
"""
from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    #url(r'^$', 'cars.views.cars_view', name='cars'),
    url(r'^$',  views.CarView.as_view(), name='cars'),
)
