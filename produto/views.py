from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request, 'home.html')

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produto': produtos})
# Compare this snippet from produto/models.py: