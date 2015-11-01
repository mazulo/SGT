from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login as django_login, logout as django_logout,
    get_user_model
)
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, AuthenticationForm, EditUserDbvForm


User = get_user_model()


def login(request):
    template_name = 'accounts/login.html'
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
                return redirect('accounts:dashboard')
    else:
        form = AuthenticationForm()
    context_dict['form'] = form
    return render(request, template_name, context_dict)


def register(request):
    template_name = 'accounts/register.html'
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


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context_dict = {
        'payments': request.user.payments.all()
    }
    return render(request, template_name, context_dict)


@login_required
def edit(request):
    context = {}
    template_name = 'accounts/edit.html'
    if request.method == 'POST':
        form = EditUserDbvForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = EditUserDbvForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


def list_dbvs(request):
    template_name = 'accounts/list_dbvs.html'
    dbvs = User.objects.all().exclude(is_admin=True)
    context_dict = {
        'dbvs': dbvs
    }
    return render(request, template_name, context_dict)


def dbv_view(request, pk):
    template_name = 'accounts/dbv.html'
    context_dict = {}
    dbv = User.objects.get(pk=pk)
    payments = dbv.payments.all().count()
    context_dict['dbv'] = dbv
    context_dict['payments'] = payments
    return render(request, template_name, context_dict)
