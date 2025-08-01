from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.UserLogin.as_view(), name = "login"),
    path("signup/", views.UserSignup.as_view(), name = "signup"),
    path("logout", views.simple_logout, name = "logout"),
]