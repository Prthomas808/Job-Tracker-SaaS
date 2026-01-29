from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Application

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class AddApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
        widgets = {
            "applied" : forms.DateInput(attrs={"type" : "date"}),
            "notes" : forms.Textarea(attrs={"rows" : 5 ,"cols" : 5}),
        }