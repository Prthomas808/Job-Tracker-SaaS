from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="core/auth/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
]
