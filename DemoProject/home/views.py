from django.shortcuts import render
from django.http import HttpResponse
from . import forms
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