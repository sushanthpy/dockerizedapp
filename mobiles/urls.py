"""
URLs for the cars app.
"""
from django.conf.urls import patterns, url

from mobiles import views

urlpatterns = [url(r'^$', views.MobileView.as_view(), name='mobiles')]
