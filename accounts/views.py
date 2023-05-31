from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import FormView


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = ['username', 'password']
    success_url = '/'


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
