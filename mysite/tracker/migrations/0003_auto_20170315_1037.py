# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20170309_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='page_interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('current_page', models.CharField(max_length=1000)),
                ('buttons_clicked', models.TextField(blank=True, default=False)),
                ('coordinates', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='buttons_clicked',
        ),
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='coordinates',
        ),
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='current_page',
        ),
        migrations.RemoveField(
            model_name='itc_user_interaction',
            name='page_visited',
        ),
        migrations.AddField(
            model_name='itc_user_interaction',
            name='session_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='itc_user_interaction',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
    ]
