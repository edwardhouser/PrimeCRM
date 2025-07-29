from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm



# Create your views here.

class UserLogin(LoginView):
    template_name = "crm/registration/login.html"

    def get_success_url(self):
        return reverse('home')
    

class UserSignup(CreateView):
    template_name = "crm/registration/signup.html"
    success_url = reverse_lazy("login")
    form_class = UserRegisterForm

class UserLogout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')


def simple_logout(request):
    logout(request)
    return redirect('login')