# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-23 23:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20191123_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='gform',
            name='form_desc',
        ),
        migrations.RemoveField(
            model_name='gform',
            name='form_name',
        ),
        migrations.RemoveField(
            model_name='question',
            name='form',
        ),
        migrations.AddField(
            model_name='gform',
            name='gform_desc',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='gform',
            name='gform_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='gform',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.Gform'),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
