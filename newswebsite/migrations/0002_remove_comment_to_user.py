# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-13 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newswebsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='to_user',
        ),
    ]