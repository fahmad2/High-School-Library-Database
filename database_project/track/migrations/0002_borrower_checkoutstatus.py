# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='checkOutStatus',
            field=models.BooleanField(default=False),
        ),
    ]
