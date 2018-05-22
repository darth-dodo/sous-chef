# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# system imports
from django.db import models

# app imports
from recipes.utils.model_utils import RowInformation
from recipes.constants import CATEGORIES, RECIPE_DIFFICULTY, INGREDIENT_AVAILABILITY, LOCALLY, MAINS, MEDIUM


# Create your models here.

class Ingredient(RowInformation):
    name = models.CharField(max_length=100, required=True, unique=True)
    cost = models.CharField(max_length=2, choices=INGREDIENT_AVAILABILITY, default=LOCALLY)
    low_shelf_life = models.BooleanField(default=False)

    class Meta:
        db_table = 'ingredients'

    def save(self, *args, **kwargs):
        self.name = self.name.title

    def __str__(self):
        return "{0}".format(self.name)


class Recipe(RowInformation):
    """
    Stores recipes
    """
    name = models.CharField(max_length=100, required=True)
    url = models.URLField(null=True, blank=True)
    is_veg = models.BooleanField(default=False)

    category = models.CharField(max_length=2, choices=CATEGORIES, required=True, default=MAINS)
    difficulty = models.CharField(max_length=2, choices=RECIPE_DIFFICULTY, required=MEDIUM)

    description = models.TextField(null=True, blank=True)

    # associations
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients', blank=True)

    # denormalized
    steps = models.TextField(null=True, blank=True)
    servings = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'recipes'

    def save(self, *args, **kwargs):
        self.name = self.name.title

    def __str__(self):
        return "{0}".format(self.name)


class NutritionalInformation(RowInformation):
    """
    
    """
    recipe = models.OneToOneField(Recipe, related_name='recipe', on_delete=models.CASCADE)
    fats = models.PositiveIntegerField(default=0)
    protein = models.PositiveIntegerField(default=0)
    carbs = models.PositiveIntegerField(default=0)
    fibre = models.PositiveIntegerField(default=0)
    net_carbs = models.PositiveIntegerField(default=0)

    calories = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'nutritional_information'

    def __str__(self):
        return '{0} kcals'.format(self.calories)

    def save(self, *args, **kwargs):
        if not self.net_carbs:
            self.net_carbs = self.carbs - self.fibre
