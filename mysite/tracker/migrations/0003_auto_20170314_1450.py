# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20170309_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='page_interaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('session_id', models.IntegerField()),
                ('current_page', models.CharField(max_length=1000)),
                ('buttons_clicked', models.TextField(default=False, blank=True)),
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
            field=models.IntegerField(default=datetime.datetime(2017, 3, 14, 12, 50, 30, 988036, tzinfo=utc)),
            preserve_default=False,
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
    ]
