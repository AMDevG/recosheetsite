from django.conf.urls import include, url
from recoapp import views

urlpatterns = [
    url(r'^$', views.reco, name='reco'),
    url(r'^list/$', views.list, name='list')
]