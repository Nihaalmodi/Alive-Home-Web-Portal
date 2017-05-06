# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonimport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='time',
            field=models.CharField(choices=[('8am-8:55am', '8am-8:55am'), ('9am-9:55am', '9am-9:55am'), ('10am-10:55am', '10am-10:55am'), ('11am-11:55am', '11am-11:55am'), ('12pm-12:55pm', '12pm-12:55pm'), ('1pm-1:55pm', '1pm-1:55pm'), ('2pm-2:55pm', '2pm-2:55pm'), ('3pm-3:55pm', '3pm-3:55pm'), ('4pm-4:55pm', '4pm-4:55pm'), ('5pm-5:55pm', '5pm-5:55pm')], default='8:00am-8:55am', max_length=20),
        ),
    ]