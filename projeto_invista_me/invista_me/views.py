from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def pagina_inicial(request):
    return HttpResponse('Agora vai!')


def contato(request):
    return HttpResponse('Nosso telefone é 6199651-1980')

