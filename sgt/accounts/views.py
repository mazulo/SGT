from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login as django_login, logout as django_logout
)

from .forms import RegistrationForm, AuthenticationForm


def login(request):
    template_name = 'register/login.html'
    context_dict = {}
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                django_login(request, user)
                return redirect('core:index')
    else:
        form = AuthenticationForm()
    context_dict['form'] = form
    return render(request, template_name, context_dict)


def register(request):
    template_name = 'register/register.html'
    context_dict = {}
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = RegistrationForm()
    context_dict['form'] = form
    return render(request, template_name, context_dict)


def logout(request):
    django_logout(request)
    return redirect('core:index')
