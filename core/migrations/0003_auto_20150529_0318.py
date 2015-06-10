# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150529_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalidade',
            name='status_pagamento',
            field=models.BooleanField(default=False),
        ),
    ]
