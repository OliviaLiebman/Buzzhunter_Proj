# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20170314_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='user_name',
        ),
    ]
