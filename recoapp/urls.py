from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^reco/$', views.reco, name="reco"),
    url(r'success/$',views.success, name="success")
]