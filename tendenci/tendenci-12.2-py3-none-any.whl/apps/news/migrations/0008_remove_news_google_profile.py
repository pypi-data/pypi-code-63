# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-15 15:12


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20180315_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='google_profile',
        ),
    ]
