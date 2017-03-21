# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0014_itc_user_interaction_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='itc_user_interaction',
            name='date_time_of_access',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 15, 8, 1, 38, 886612, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
