from django.urls import path
from . import views

urlpatterns = [
    # ... outras URLs ...
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('realizar_login/', views.realizar_login, name='realizar_login'),
]