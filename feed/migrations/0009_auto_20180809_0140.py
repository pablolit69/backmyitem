# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_auto_20180809_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report_item',
            name='category',
        ),
        migrations.AlterField(
            model_name='report_item',
            name='title',
            field=models.CharField(help_text='*Title for the post e.g. item identity', max_length=255),
        ),
    ]
