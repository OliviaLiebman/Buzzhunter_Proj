# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0023_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='page_interaction',
            name='session_id',
        ),
    ]
