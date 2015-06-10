# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150529_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalidade',
            name='desbravador',
            field=models.ForeignKey(related_name='mensalidades', to='core.Desbravador'),
        ),
    ]
