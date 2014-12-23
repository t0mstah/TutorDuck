# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorBase', '0002_auto_20141222_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.IntegerField(default='import os'),
            preserve_default=False,
        ),
    ]
