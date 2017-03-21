# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_itc_user_interaction_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='session',
        ),
    ]
