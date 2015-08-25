# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdbv',
            name='team',
            field=models.ForeignKey(null=True, to='core.Team', related_name='dbvs'),
        ),
        migrations.AddField(
            model_name='userdbv',
            name='user_permissions',
            field=models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.', to='auth.Permission', related_query_name='user', verbose_name='user permissions', blank=True),
        ),
    ]
