# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorBase', '0004_auto_20141223_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorcard',
            name='phone',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.IntegerField(default=b'h\x93oww\x8a\x9f\x08\xeak\xc1\xb6\r\xe9K}\x9d\x1aY\xac\x88\x15\xa2(\xfa\xf83F \xd6\xcb\xc5y\xd0Q>\xa5>&\x19[\xf3q\x92\x1f4\x87\x80\x07\x02'),
            preserve_default=True,
        ),
    ]
