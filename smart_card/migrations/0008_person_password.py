# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-15 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_card', '0007_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='password', max_length=15),
            preserve_default=False,
        ),
    ]
