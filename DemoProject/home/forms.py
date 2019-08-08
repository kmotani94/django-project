from django import forms
from .models import User


class FormName(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = "__all__"