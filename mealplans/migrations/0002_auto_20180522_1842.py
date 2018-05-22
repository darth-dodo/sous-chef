# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 13:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mealplans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMealPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('meal_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_mealplan', to='mealplans.MealPlan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_mealplan', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_mealplan',
                'verbose_name_plural': 'User Mealplans',
            },
        ),
        migrations.AlterUniqueTogether(
            name='usermealplan',
            unique_together=set([('user', 'meal_plan')]),
        ),
    ]