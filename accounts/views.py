from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegisterForm
from django.urls import reverse_lazy


class LoginView(CreateView):
    model = User
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('product:product_list')


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('product:product_list')


# class PasswordChangeView(CreateView):
#     model = User
#     form_class = PasswordChangeForm
#     template_name = 'accounts/register.html'
#     success_url = reverse_lazy('product:product_list')
