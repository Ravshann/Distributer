# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-17 10:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default=datetime.datetime(2017, 1, 17, 10, 38, 35, 202611, tzinfo=utc), max_length=255, verbose_name='Order ID'),
            preserve_default=False,
        ),
    ]
