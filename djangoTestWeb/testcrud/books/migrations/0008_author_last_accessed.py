# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_publisher_last_accessed'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_accessed',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 13, 21, 43, 921000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
