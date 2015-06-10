from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)
from django.core import validators
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-mail', unique=True)
    username = models.CharField(
        'Nome de Usuário',
        max_length=30,
        unique=True,
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                (
                    'Enter a valid username. This value may contain only ',
                    'letters, numbers ' 'and @/./+/-/_ characters.'
                )
            ),
        ],
    )
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField(
        'Data de entrada',
        default=timezone.now
    )
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)


class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    historia = models.TextField(blank=True)
    imagem_perfil = models.ImageField(
        upload_to='unity_profile_images', blank=True
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Desbravador(CustomUser):

    CARGO_CHOICES = (
        ('CSO', 'Conselheiro(a)'),
        ('CPT', 'Capit(ã)o'),
        ('SCT', 'Secretário(a)'),
        ('TSR', 'Tesoureiro(a)'),
        ('INS', 'Instrutor(a)'),
        ('DRT', 'Diretor(a)'),
        ('DRT_AS', 'Diretor(a) Associado(a)'),
        ('CPL', 'Capel(ã)o'),
    )

    nome = models.CharField('Nome completo', max_length=100)
    idade = models.IntegerField()
    imagem_perfil = models.ImageField(
        upload_to='dbv_profile_images', blank=True
    )
    unidade = models.ForeignKey(Unidade, related_name='desbravador')
    cargo = models.CharField(max_length=100, choices=CARGO_CHOICES)

    def __str__(self):
        return '{}'.format(self.nome or self.username)

    class Meta:
        verbose_name = 'Desbravador'
        verbose_name_plural = 'Desbravadores'
        ordering = ['unidade']


class Mensalidade(models.Model):
    mes = models.DateField()
    desbravador = models.ForeignKey(
        Desbravador, related_name='mensalidades'
    )
    status_pagamento = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Mensalidade'
        verbose_name_plural = 'Mensalidades'
        ordering = ['mes']

    def __str__(self):
        return ('{} - {}'.format(self.mes, self.desbravador))
