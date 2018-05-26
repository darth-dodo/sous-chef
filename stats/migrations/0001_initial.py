# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 03:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DayVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'day_variant',
            },
        ),
        migrations.CreateModel(
            name='WeightLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('calories_consumed', models.PositiveIntegerField(default=0)),
                ('my_fitness_plan_entry', models.URLField(blank=True, null=True)),
                ('weight', models.FloatField()),
                ('day_variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weight_logs', to='stats.DayVariant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weight_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'weight_log',
            },
        ),
        migrations.AlterUniqueTogether(
            name='weightlog',
            unique_together=set([('date', 'user')]),
        ),
    ]