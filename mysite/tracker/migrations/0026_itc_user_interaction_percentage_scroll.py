# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0025_auto_20170316_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='itc_user_interaction',
            name='percentage_scroll',
            field=models.CharField(default=datetime.datetime(2017, 3, 19, 10, 13, 44, 796512, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
