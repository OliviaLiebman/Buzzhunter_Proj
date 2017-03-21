# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('tracker', '0008_auto_20170314_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='itc_user_interaction',
            name='session',
            field=models.ForeignKey(default=1, to='sessions.Session'),
        ),
    ]
