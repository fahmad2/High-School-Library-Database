# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_borrower_checkoutstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='checkOutStatus',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]