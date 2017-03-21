# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0030_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='heatmap',
            name='current_page',
            field=models.CharField(default=b'unknown', max_length=1000),
        ),
    ]
