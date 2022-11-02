from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def pagina_inicial(request):
    return HttpResponse('VOU CONSEGUIR!')


def contato(request):
    return HttpResponse('Nosso telefone é XX XXXXXXXXXXX')

def minha_historia(request):
    pessoa = {
        'nome': 'Cláudio',
        'idade': 42,
        'profissao': 'professor'

    }
    return render(request, 'investimentos/minha_historia.html', pessoa )