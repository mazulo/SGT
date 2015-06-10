# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.contrib.auth.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail', unique=True)),
                ('username', models.CharField(max_length=30, verbose_name='Nome de Usuário', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', ('Enter a valid username. This value may contain only ', 'letters, numbers and @/./+/-/_ characters.'))])),
                ('is_active', models.BooleanField(verbose_name='Está ativo?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='É da equipe?', default=False)),
                ('date_joined', models.DateTimeField(verbose_name='Data de entrada', default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Mensalidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('mes', models.DateField()),
                ('status_pagamento', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Mensalidade',
                'ordering': ['mes'],
                'verbose_name_plural': 'Mensalidades',
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('historia', models.TextField(blank=True)),
                ('imagem_perfil', models.ImageField(blank=True, upload_to='unity_profile_images')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Desbravador',
            fields=[
                ('customuser_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('idade', models.IntegerField()),
                ('imagem_perfil', models.ImageField(blank=True, upload_to='dbv_profile_images')),
                ('cargo', models.CharField(max_length=100, choices=[('CSO', 'Conselheiro(a)'), ('CPT', 'Capit(ã)o'), ('SCT', 'Secretário(a)'), ('TSR', 'Tesoureiro(a)'), ('INS', 'Instrutor(a)'), ('DRT', 'Diretor(a)'), ('DRT_AS', 'Diretor(a) Associado(a)'), ('CPL', 'Capel(ã)o')])),
                ('unidade', models.ForeignKey(to='core.Unidade', related_name='desbravador')),
            ],
            options={
                'verbose_name': 'Desbravador',
                'ordering': ['unidade'],
                'verbose_name_plural': 'Desbravadores',
            },
            bases=('core.customuser',),
        ),
        migrations.AddField(
            model_name='mensalidade',
            name='desbravador',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='mensalidade'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', verbose_name='groups', related_name='user_set', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', verbose_name='user permissions', related_name='user_set', related_query_name='user', help_text='Specific permissions for this user.', blank=True),
        ),
    ]
