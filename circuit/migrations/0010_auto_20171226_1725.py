# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuit', '0009_auto_20171226_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homedetail',
            name='Fax',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='homedetail',
            name='Mobile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
