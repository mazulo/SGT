from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.contrib.auth import login

# from .models import Unidade, Mensalidade


def index(request):
    return render(request, 'core/index.html', {})


# def list_dbvs(request):
#     dict_context = {}
#     dbvs = Desbravador.objects.all()
#     dict_context['dbvs'] = dbvs
#     return render(request, 'core/list_dbvs.html', dict_context)


# def list_unidades(request):
#     dict_context = {}
#     unidades = Unidade.objects.all()
#     dict_context['unidades'] = unidades
#     return render(request, 'core/list_unities.html', dict_context)


# def list_mensalidade(request, user_dbv):
#     dict_context = {}
#     dbv = Desbravador.objects.get(username=user_dbv)
#     mensalidade = get_object_or_404(Mensalidade, desbravador=dbv)
#     dict_context['mensalidade'] = mensalidade
#     return render(request, 'core/list_mensalidade.html', dict_context)
