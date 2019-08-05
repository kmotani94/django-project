from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("HOME PAGE")


def about(request):
    return HttpResponse("ABOUT PAGE")


def gallery(response):
    return HttpResponse("GALLERY PAGE")