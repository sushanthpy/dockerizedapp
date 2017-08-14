"""
URLs for the mdb project.
"""
from django.conf.urls import include, url


urlpatterns = [
    url(r'mobiles/', include('mobiles.urls'))
]
