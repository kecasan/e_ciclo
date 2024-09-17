from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione quaisquer campos adicionais que você queira aqui.
    # Por exemplo, você pode adicionar um campo para o número de telefone do usuário.
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.usuario.username
