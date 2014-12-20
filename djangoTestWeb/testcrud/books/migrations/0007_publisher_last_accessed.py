# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_author_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='last_accessed',
            field=models.DateField(default=datetime.datetime(2014, 12, 17, 13, 19, 23, 546000, tzinfo=utc), verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe8\xae\xbf\xe9\x97\xae\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=False,
        ),
    ]
