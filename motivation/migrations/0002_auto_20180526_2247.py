# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 17:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('motivation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivationRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'motivation_rating',
            },
        ),
        migrations.AlterModelOptions(
            name='motivationcategory',
            options={'verbose_name_plural': 'Motivational categories'},
        ),
        migrations.AddField(
            model_name='motivationalstuff',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='motivation.MotivationRating'),
        ),
    ]
