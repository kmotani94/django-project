from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from . import forms
from .models import User
from .serializers import LoginSerializer

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

def signUp(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            # print("Username: " + form.cleaned_data["username"])
            # print(request.POST.get("username"))
            form.save()
    context = {"signup_page": "active", "signup_form": form}  # new info here
    return render(request, 'home/signup.html', context)

class LoginList(APIView):
    def get(self, request):
        values = User.objects.all()
        serializer = LoginSerializer(values, many=True)
        return Response(serializer.data)