from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

  if request.method == 'POST':
    print(f'Método: {request.method}')

  return HttpResponse('Hello CORE!')


def hello(request):
  return HttpResponse('Hello Django')


def hello_rosa(request):
  return HttpResponse('Vc é um Rosa!')


def milhao(request):
  return HttpResponse('Faça um milhão com Django!')
