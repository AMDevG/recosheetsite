# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-24 04:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recoapp', '0002_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='parent_id',
        ),
    ]
