# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20141214_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='sex',
        ),
    ]
