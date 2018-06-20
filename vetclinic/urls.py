from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.record_list, name='record_list'),
    url(r'^(?P<url>.*)/$', views.record_list_filtered, name='record_list_filtered')
]