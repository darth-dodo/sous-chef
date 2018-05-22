# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_ingredients_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_duration',
            field=models.PositiveIntegerField(default=0),
        ),
    ]