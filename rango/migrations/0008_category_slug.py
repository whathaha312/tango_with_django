# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20141112_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2014, 11, 12, 22, 8, 47, 589569, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
