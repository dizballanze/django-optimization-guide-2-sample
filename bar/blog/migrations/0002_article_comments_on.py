# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments_on',
            field=models.BooleanField(default=True),
        ),
    ]
