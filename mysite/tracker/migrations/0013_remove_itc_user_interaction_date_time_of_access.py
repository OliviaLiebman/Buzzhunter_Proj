# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_itc_user_interaction_date_time_of_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='date_time_of_access',
        ),
    ]
