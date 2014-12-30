# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorBase', '0005_departments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Departments',
        ),
    ]
