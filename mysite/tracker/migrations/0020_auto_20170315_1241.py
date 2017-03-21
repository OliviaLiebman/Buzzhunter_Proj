# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0019_auto_20170315_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='itc_user_interaction',
            name='session_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='page_interaction',
            name='session_id',
            field=models.IntegerField(default=1),
        ),
    ]
