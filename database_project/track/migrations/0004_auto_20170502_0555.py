# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_auto_20170502_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='check_out_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='track.Borrower'),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='checkOutStatus',
            field=models.BooleanField(default=False),
        ),
    ]
