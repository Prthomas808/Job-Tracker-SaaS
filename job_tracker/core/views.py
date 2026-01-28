from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def register_view(request):
    if request.POST == "Post":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "core/auth/register.html", {"form" : form})
