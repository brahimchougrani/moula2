# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuit', '0005_homedetail_logo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homedetail',
            name='logo_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
