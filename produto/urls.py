from django.urls import path
from .views import lista_produtos, views

urlpatterns = [
    path("", views.home, name='home'),
    path("produtos/", lista_produtos, name='lista_produtos'),
]