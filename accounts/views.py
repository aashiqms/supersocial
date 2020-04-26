from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


sign_up_view = SignUp.as_view()
log_in_view = LoginView.as_view(template_name="registration/login.html")
log_out_view = LogoutView.as_view()
