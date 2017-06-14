# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-14 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_card', '0002_auto_20170614_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.CharField(max_length=1)),
                ('district_id', models.CharField(max_length=2)),
                ('district_name', models.CharField(max_length=150)),
            ],
        ),
    ]
