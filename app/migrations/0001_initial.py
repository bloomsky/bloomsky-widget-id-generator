# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-26 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IDReference',
            fields=[
                ('device_id', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('widget_id', models.CharField(blank=True, max_length=8, null=True, unique=True)),
            ],
        ),
    ]
