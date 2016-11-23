from django.conf.urls import include, url
from . import views

urlpatterns = [



    url (r'^$', views.compra_nueva, name='compra_nueva'),


]
