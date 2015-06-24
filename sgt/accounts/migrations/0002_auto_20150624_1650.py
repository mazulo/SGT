# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('core', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdbv',
            name='group',
            field=models.ForeignKey(related_name='desbravadores', to='core.Unidade', null=True),
        ),
        migrations.AddField(
            model_name='userdbv',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', to='auth.Group', blank=True, verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userdbv',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', help_text='Specific permissions for this user.', related_name='user_set', to='auth.Permission', blank=True, verbose_name='user permissions'),
        ),
    ]
