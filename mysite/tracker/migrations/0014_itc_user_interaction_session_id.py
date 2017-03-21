# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_remove_itc_user_interaction_date_time_of_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='itc_user_interaction',
            name='session_id',
            field=models.IntegerField(default=1),
        ),
    ]
