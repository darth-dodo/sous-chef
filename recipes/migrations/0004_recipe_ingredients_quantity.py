# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20180522_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients_quantity',
            field=models.TextField(blank=True, null=True),
        ),
    ]