# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# system imports
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# project imports
from cookit.utils.model_utils import RowInformation
# Create your models here.


class DayVariant(RowInformation):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'day_variant'

    def save(self, *args, **kwargs):
        super(DayVariant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class WeightLog(RowInformation):
    weight = models.FloatField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    user = models.ForeignKey(User, blank=False, null=False, related_name='weight_logs')
    day_variant = models.ForeignKey(DayVariant, blank=True, null=True, related_name='weight_logs')
    calories_consumed = models.PositiveIntegerField(default=0)
    my_fitness_plan_entry = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'weight_log'
        unique_together = ['date', 'user']

    @classmethod
    def from_db(cls, db, field_names, values):
        new = super(WeightLog, cls).from_db(db, field_names, values)
        # cache value went from the base
        new._updated_user_id = values[field_names.index('user_id')]
        return new

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        """
        """

        self.weight = round(self.weight, 2)

        if hasattr(self, '_updated_user_id'):

            if not self._state.adding and self._updated_user_id != self.user_id:
                # cannot update the user id
                raise ValidationError("You cannot update the User!")

        super(WeightLog, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} | {1} | {2} kgs".format(self.user, self.date, self.weight)
