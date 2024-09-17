from django.urls import path
from . import  views

urlpatterns = [
    path("", views.home, name='home'),
    path("produtos/", views.lista_produtos, name='lista_produtos'),
]