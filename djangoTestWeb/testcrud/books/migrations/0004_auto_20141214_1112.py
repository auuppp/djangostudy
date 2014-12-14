# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20141206_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='sex',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=60, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x9b\xbd\xe5\xae\xb6'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='state_province',
            field=models.CharField(max_length=30, verbose_name=b'\xe7\x9c\x81\xe4\xbb\xbd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(null=True, verbose_name=b'\xe7\xbd\x91\xe5\x9d\x80', blank=True),
            preserve_default=True,
        ),
    ]
