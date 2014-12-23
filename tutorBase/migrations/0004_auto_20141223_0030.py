# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorBase', '0003_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorcard',
            name='phone',
            field=models.IntegerField(default=b'h\xcaL\xe6\xea\xff\xf0&\x0e\x87\xb7\x07\\\xcb\xeb\x1b\xa81I\xac\x02944\xa8\x1fKV\xa8\x9a3E0\x86P\x11Z\x88\xb3:\xefj\xc8\xc3\x0b\xa5_\x16\xf6\xa8'),
            preserve_default=True,
        ),
    ]
