# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorBase', '0002_auto_20141223_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorcard',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='tutorcard',
            name='rate',
        ),
    ]
