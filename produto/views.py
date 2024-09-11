from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request, 'home.html')

#def produto(request, id):
def lista_produtos(request):
#    if not request.session.get('carrinho'):
#        request.session['carrinho'] = []
#        request.session.save()
#    erro = request.GET.get('erro')
#    produtos = Produto.objects.filter(id=id)[0]
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produto': produtos})
                                            #'carrinho': len(request.session['carrinho'])})
                                            #'erro': erro})
