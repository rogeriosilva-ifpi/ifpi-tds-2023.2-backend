from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    if request.method == 'POST':
        print(f'Método: {request.method}')

    # return HttpResponse('Hello CORE!')
    return render(request, template_name='core/teste.html')


def hello(request):
    return HttpResponse('Hello Django')


def hello_rosa(request):
    return HttpResponse('Vc é um Rosa!')


def milhao(request):
    return HttpResponse('Faça um milhão com Django!')
