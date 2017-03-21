# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0031_heatmap_current_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itc_user_interaction',
            name='user_id',
            field=models.CharField(default=b'N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='page_interaction',
            name='user_id',
            field=models.CharField(default=b'N/A', max_length=100),
        ),
    ]
