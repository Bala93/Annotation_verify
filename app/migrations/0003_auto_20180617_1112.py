# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-17 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180617_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docinfo',
            name='iscomplete',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='docinfo',
            name='iscorrect',
            field=models.CharField(max_length=10),
        ),
    ]
