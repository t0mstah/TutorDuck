# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorBase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorcard',
            old_name='tagline',
            new_name='tagLine',
        ),
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
