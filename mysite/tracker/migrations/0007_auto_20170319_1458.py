# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-19 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20170319_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itc_user_interaction',
            name='overall_time',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]