from django.conf.urls import include, url
from . import views

urlpatterns = [
   # url(r'success/$',views.success, name="success"),
    url(r'^$', views.reco, name='reco')
]