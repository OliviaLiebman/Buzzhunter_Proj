# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20170319_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='heatmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coordinate', models.IntegerField(default=1)),
                ('y_coordinate', models.IntegerField(default=1)),
                ('current_page', models.CharField(default='unknown', max_length=1000)),
            ],
        ),
    ]
