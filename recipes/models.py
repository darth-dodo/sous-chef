# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# system imports
from django.db import models

# project imports
from cookit.utils.model_utils import RowInformation

# app imports
from recipes.constants import CATEGORIES, RECIPE_DIFFICULTY, INGREDIENT_AVAILABILITY, LOCALLY, MAINS, MEDIUM


class Ingredient(RowInformation):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    availability = models.CharField(max_length=2, choices=INGREDIENT_AVAILABILITY, default=LOCALLY)
    low_shelf_life = models.BooleanField(default=True)

    class Meta:
        db_table = 'ingredients'

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Recipe(RowInformation):
    """
    Stores recipes
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    url = models.URLField(null=True, blank=True)
    is_veg = models.BooleanField(default=False)

    category = models.CharField(max_length=2, choices=CATEGORIES, default=MAINS)
    difficulty = models.CharField(max_length=2, choices=RECIPE_DIFFICULTY, default=MEDIUM)

    description = models.TextField(null=True, blank=True)

    # associations
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients', blank=True)

    # denormalized
    ingredients_quantity = models.TextField(null=True, blank=True)

    steps = models.TextField(null=True, blank=True)
    cooking_duration = models.PositiveIntegerField(default=0)

    servings = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'recipes'

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return "{0}".format(self.name)


class NutritionalInformation(RowInformation):
    """
    
    """
    recipe = models.OneToOneField(Recipe, related_name='stats', on_delete=models.CASCADE)
    fats = models.PositiveIntegerField(default=0)
    protein = models.PositiveIntegerField(default=0)
    carbs = models.PositiveIntegerField(default=0)
    fibre = models.PositiveIntegerField(default=0)
    net_carbs = models.PositiveIntegerField(default=0)

    calories = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'nutritional_information'
        verbose_name_plural = 'Nutrional Information'

    def __str__(self):
        return '{0} | {1} servings | {2} kcals'.format(
            self.recipe.name, self.recipe.servings, self.calories)

    def save(self, *args, **kwargs):
        if not self.net_carbs:
            self.net_carbs = self.carbs - self.fibre

        super(NutritionalInformation, self).save(*args, **kwargs)
