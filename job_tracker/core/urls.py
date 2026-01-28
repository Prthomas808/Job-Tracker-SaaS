from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", auth_view.LoginView.as_view(template_name="core/auth/login.html"), name="login"),
]
