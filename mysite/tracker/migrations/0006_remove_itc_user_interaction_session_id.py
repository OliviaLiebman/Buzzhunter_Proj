# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20170314_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='session_id',
        ),
    ]
