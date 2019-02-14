# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-12-21 03:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181221_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='block',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='block', to='users.Area', verbose_name='区'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='city', to='users.Area', verbose_name='市'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro', to='users.Area', verbose_name='省'),
        ),
    ]
