from django.conf.urls import include, url
from recoapp import views

urlpatterns = [
    url(r'^reco/$', views.reco, name='reco')
]