# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-24 05:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20191124_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='gform',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.Gform'),
        ),
    ]
