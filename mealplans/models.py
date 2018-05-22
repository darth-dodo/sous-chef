# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# system imports
from django.db import models
from django.contrib.auth.models import User

# project imports
from cookit.utils.model_utils import RowInformation

# app imports
from mealplans.utils.constants import DAYS_OF_THE_WEEK, MEALS
from mealplans.utils.mealplan_utils import calculate_approx_calories_for_recipes


class MealPlan(RowInformation):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'mealplan'

    def save(self, *args, **kwargs):
        super(MealPlan, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class MealPlanMenu(RowInformation):
    meal_plan = models.ForeignKey(MealPlan, related_name='mealplan')
    day = models.CharField(max_length=2, choices=DAYS_OF_THE_WEEK, null=False, blank=False)
    meal = models.CharField(max_length=2, choices=MEALS, null=False, blank=False)
    approx_calorie_count = models.PositiveIntegerField(default=0)
    recipes = models.ManyToManyField('recipes.Recipe', related_name='mealplan_recipes')

    class Meta:
        db_table = 'mealplan_menu'
        verbose_name_plural = 'MealPlan Menu'
        unique_together = ['day', 'meal_plan', 'meal']

    def save(self, *args, **kwargs):

        # if not self.approx_calorie_count:
        #     self.approx_calorie_count = calculate_approx_calories_for_recipes(self.recipes)

        super(MealPlanMenu, self).save(*args, **kwargs)

    def __str__(self):
        return '{0} - {1}'.format(self.meal_plan, self.get_day_display())


class UserMealPlan(RowInformation):
    user = models.ForeignKey(User, related_name='user_mealplan')
    meal_plan = models.ForeignKey(MealPlan, related_name='user_mealplan')

    class Meta:
        db_table = 'user_mealplan'
        verbose_name_plural = 'User Mealplans'
        unique_together = ['user', 'meal_plan']

    def save(self, *args, **kwargs):
        super(UserMealPlan, self).save(*args, **kwargs)

    def __str__(self):
        return '{0} - {1}'.format(self.user.username, self.meal_plan.name)
