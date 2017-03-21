# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_remove_itc_user_interaction_session_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page_interaction',
            name='session_id',
        ),
    ]
