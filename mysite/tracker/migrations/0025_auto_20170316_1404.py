# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0024_auto_20170316_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='itc_user_interaction',
            name='session_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='itc_user_interaction',
            name='user_email',
            field=models.CharField(default=b'Email', max_length=100),
        ),
        migrations.AddField(
            model_name='itc_user_interaction',
            name='user_name',
            field=models.CharField(default=b'User', max_length=100),
        ),
        migrations.AddField(
            model_name='page_interaction',
            name='session_id',
            field=models.IntegerField(default=1),
        ),
    ]
