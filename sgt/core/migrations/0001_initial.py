# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('mes', models.DateField()),
                ('status_pagamento', models.BooleanField(default=False)),
                ('desbravador', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='mensalidades')),
            ],
            options={
                'verbose_name_plural': 'Mensalidades',
                'ordering': ['mes'],
                'verbose_name': 'Mensalidade',
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('historia', models.TextField(blank=True)),
                ('imagem_perfil', models.ImageField(blank=True, upload_to='unity_profile_images')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
