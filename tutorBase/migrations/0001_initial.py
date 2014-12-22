# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TutorCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('tagline', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('rate', models.CommaSeparatedIntegerField(max_length=10)),
                ('phone', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tutorcard',
            name='tutor',
            field=models.ForeignKey(to='tutorBase.User'),
            preserve_default=True,
        ),
    ]
