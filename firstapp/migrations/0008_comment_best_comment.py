# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_comment_belong_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='best_comment',
            field=models.BooleanField(default=False),
        ),
    ]
