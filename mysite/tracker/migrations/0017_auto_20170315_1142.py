# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0016_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page_interaction',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
    ]
