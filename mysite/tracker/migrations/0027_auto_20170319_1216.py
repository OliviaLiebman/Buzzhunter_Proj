# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0026_itc_user_interaction_percentage_scroll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itc_user_interaction',
            name='percentage_scroll',
            field=models.CharField(default=b'No Scroll', max_length=100),
        ),
    ]
