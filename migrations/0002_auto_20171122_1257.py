# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-22 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mt_users',
            name='f_email_id',
            field=models.CharField(default='email', max_length=1000),
        ),
    ]
