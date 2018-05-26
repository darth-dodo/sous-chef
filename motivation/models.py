# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# system imports
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from cookit.utils.model_utils import RowInformation


class MotivationCategory(RowInformation):
    created_by = models.ForeignKey(User)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        db_table = 'motivation_category'
        verbose_name_plural = 'Motivational categories'

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(MotivationCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class MotivationRating(RowInformation):
    created_by = models.ForeignKey(User)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        db_table = 'motivation_rating'

    def save(self, *args, **kwargs):
        super(MotivationRating, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class MotivationalStuff(RowInformation):

    created_by = models.ForeignKey(User)
    category = models.ForeignKey(MotivationCategory, related_name='motivational_stuff')
    rating = models.ForeignKey(MotivationRating, null=True, blank=True)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'motivational_stuff'

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(MotivationalStuff, self).save(*args, **kwargs)

    def __str__(self):
        return '{0} | {1}'.format(self.name, self.created_by)
