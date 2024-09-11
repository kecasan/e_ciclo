from django.db import models
from django.utils.safestring import mark_safe

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    img = models.ImageField(upload_to='post_img')
    preco = models.FloatField()
    descricao = models.TextField()

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/post_img/{self.img}">'


    def __str__(self):
        return self.nome_produto
