from django.db import models
from django.conf import settings


class Mensalidade(models.Model):
    mes = models.DateField()
    desbravador = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='mensalidades'
    )
    status_pagamento = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Mensalidade'
        verbose_name_plural = 'Mensalidades'
        ordering = ['mes']

    def __str__(self):
        return ('{} - {}'.format(self.mes, self.desbravador))


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
