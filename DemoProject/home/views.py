from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    dict = {'templateVariable': 'This is Jinja Variable'}
    return render(request, 'home/index.html', context=dict)


def about(request):
    return render(request, 'about/index.html', context=None)


def gallery(request):
    return render(request, 'gallery/index.html', context=None)