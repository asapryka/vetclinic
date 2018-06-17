from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.record_list, name='record_list'),
]