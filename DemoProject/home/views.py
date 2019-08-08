from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    dict = {'templateVariable': 'This is Jinja Variable'}
    context = {"home_page": "active"}  # new info here
    return render(request, 'home/home.html', context)


def about(request):
    context = {"about_page": "active"}  # new info here
    return render(request, 'home/about.html', context)


def gallery(request):
    context = {"gallery_page": "active"}  # new info here
    return render(request, 'home/gallery.html', context)