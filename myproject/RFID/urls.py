from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^log/$', views.log),
    url(r'^status/$', views.status),
    url(r'^check/(?P<serialNum>.+)/', views.check),
]
