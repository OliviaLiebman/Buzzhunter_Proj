# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='heatmap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x_coordinate', models.IntegerField(default=1)),
                ('y_coordinate', models.IntegerField(default=1)),
            ],
        ),
    ]
