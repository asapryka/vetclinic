from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.record_list, name='record_list'),
]