# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDbv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='Nome de Usuário', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', ('Enter a valid username. This value may contain only ', 'letters, numbers and @/./+/-/_ characters.'))], unique=True, max_length=30)),
                ('email', models.EmailField(verbose_name='E-mail', unique=True, max_length=254)),
                ('first_name', models.CharField(verbose_name='Primeiro Nome', max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(verbose_name='Segundo Nome', max_length=50, null=True, blank=True)),
                ('date_joined', models.DateTimeField(verbose_name='Data de entrada', auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='É da equipe?')),
                ('is_admin', models.BooleanField(default=False, verbose_name='É admin?')),
                ('age', models.IntegerField(default=10)),
                ('profile_image', models.ImageField(upload_to='dbv_profile_images', blank=True)),
                ('position', models.CharField(choices=[('CSO', 'Conselheiro(a)'), ('CPT', 'Capit(ã)o'), ('SCT', 'Secretário(a)'), ('TSR', 'Tesoureiro(a)'), ('INS', 'Instrutor(a)'), ('DRT', 'Diretor(a)'), ('DRT_AS', 'Diretor(a) Associado(a)'), ('CPL', 'Capel(ã)o')], max_length=100)),
                ('groups', models.ManyToManyField(related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', related_query_name='user', verbose_name='groups', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
