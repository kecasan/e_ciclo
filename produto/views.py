from django.shortcuts import render, redirect
from .models import Produto, Categoria
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def home_produto(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produto = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'produto.html', {'produto': produto,
                                        'carrinho': len(request.session['carrinho']),
                                        'categorias': categorias,
                                        })

def categorias(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produto = Produto.objects.filter(categoria_id = id)
    categorias = Categoria.objects.all()

    return render(request, 'home.html', {'produto': produto,
                                        'carrinho': len(request.session['carrinho']),
                                        'categorias': categorias,
                                        })

def produto(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    erro = request.GET.get('erro')
    produto = Produto.objects.filter(id=id)[0]
    categorias = Categoria.objects.all()
    return render(request, 'home_produto.html', {'id': id,
                                            'produto': produto, 
                                            'carrinho': len(request.session['carrinho']),
                                            'categorias': categorias,
                                            'erro': erro,
                                            })


def add_carrinho(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    id_produto = request.GET.get('id_produto')
    quantidade = request.GET.get('quantidade', 1)
    preco = request.GET.get('preco', 0)
    if id_produto and quantidade and preco:
        request.session['carrinho'].append(
            {'id_produto': int(id_produto),
             'quantidade': int(quantidade),
             'preco': float(preco)
             })       
    request.session.save()
    return redirect(f'/ver_carrinho') 


def ver_carrinho(request):
    categorias = Categoria.objects.all()
    dados_motrar = []
    for i in request.session['carrinho']:
        produto = Produto.objects.filter(id=i['id_produto']).first()
    if produto:
        dados_motrar.append(
            {'imagem': produto.img.url,
             'nome': produto.nome_produto,
             'quantidade': i['quantidade'],
             'preco': i['preco'],
             'id': i['id_produto']
             }
        )
    total = sum([float(i['preco']) for i in request.session['carrinho']])

    return render(request, 'carrinho.html', {'dados': dados_motrar,
                                             'total': total,
                                             'carrinho': len(request.session['carrinho']),
                                             'categorias': categorias,
                                             })
def remover_carrinho(request, id):
    if 0 <= id < len(request.session['carrinho']):
        request.session['carrinho'].pop(id)
        request.session.save()
    return redirect('/ver_carrinho')