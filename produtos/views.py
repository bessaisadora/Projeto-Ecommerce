from django.shortcuts import render
from produtos.models import Produto
from produtos.forms import UsuarioForm

def cadastro_usuario(request):
    if request.method == 'POST':
        forms = UsuarioForm(request.POST)
        if forms.is_valid():
            forms.save()
            forms = UsuarioForm()
    else:
        forms = UsuarioForm(  )
    return render (request, 'forms.html', {'form' : forms })


def base (request):
    return render(request, 'base.html')

def index(request):
	return render(request, 'index.html')

def listagem(request):
	lista = Produto.objects.all()
	context = {'produtos' : lista}
	return render(request, 'listagem.html', context)

def detalhes(request, id):
	produto = Produto.objects.get(id=id)
	context={'produto': produto}
	return render(request, 'detalhes.html', context)

def quem_somos (request):
    return render(request, 'quemsomos.html')