# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('cost', models.CharField(choices=[(b'LO', b'Locally'), (b'ON', b'Online'), (b'EX', b'Exotic')], default=b'LO', max_length=2)),
                ('low_shelf_life', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ingredients',
            },
        ),
        migrations.CreateModel(
            name='NutritionalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('fats', models.PositiveIntegerField(default=0)),
                ('protein', models.PositiveIntegerField(default=0)),
                ('carbs', models.PositiveIntegerField(default=0)),
                ('fibre', models.PositiveIntegerField(default=0)),
                ('net_carbs', models.PositiveIntegerField(default=0)),
                ('calories', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'nutritional_information',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('is_veg', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[(b'SO', b'Soups'), (b'DR', b'Desserts'), (b'AZ', b'Appetizers'), (b'MN', b'Main Course'), (b'SD', b'Side Dishes'), (b'CD', b'Condiments'), (b'SC', b'Snacks')], default=b'MN', max_length=2)),
                ('difficulty', models.CharField(choices=[(b'1', b'Easy'), (b'2', b'Medium'), (b'3', b'Hard')], default=b'2', max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
                ('steps', models.TextField(blank=True, null=True)),
                ('servings', models.PositiveIntegerField(default=1)),
                ('ingredients', models.ManyToManyField(blank=True, related_name='ingredients', to='recipes.Ingredient')),
            ],
            options={
                'db_table': 'recipes',
            },
        ),
        migrations.AddField(
            model_name='nutritionalinformation',
            name='recipe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='recipes.Recipe'),
        ),
    ]