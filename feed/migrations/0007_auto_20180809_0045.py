# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20180807_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report_item',
            name='item_name',
        ),
        migrations.AddField(
            model_name='report_item',
            name='item_type',
            field=models.CharField(default='', help_text='*Enter the item name you found e.g. Marksheet,key,wallet', max_length=100),
        ),
        migrations.AddField(
            model_name='report_item',
            name='title',
            field=models.TextField(default='', help_text='*Enter the item name you found e.g. Marksheet,key,wallet'),
        ),
        migrations.AlterField(
            model_name='report_item',
            name='city',
            field=models.CharField(help_text='*Enter the city name', max_length=20),
        ),
    ]
