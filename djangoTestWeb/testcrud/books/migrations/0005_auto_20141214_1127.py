# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20141214_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='sex',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
