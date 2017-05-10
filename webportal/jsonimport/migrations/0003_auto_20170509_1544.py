# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 15:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonimport', '0002_auto_20170506_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='room',
            field=models.CharField(blank=True, max_length=5, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]