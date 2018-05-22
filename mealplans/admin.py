# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from mealplans.models import MealPlan, MealPlanMenu, UserMealPlan


class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'description')
    search_fields = ['name']
    list_editable = ['name']

    class Meta:
        model = MealPlan


admin.site.register(MealPlan, MealPlanAdmin)


class MealPlanMenuAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'meal_plan', 'day', 'meal', 'approx_calorie_count')
    search_fields = ['meal_plan__name', 'day']
    list_filter = ['meal_plan__name', 'day']
    list_display_links = ['__str__', 'meal_plan']

    class Meta:
        model = MealPlanMenu


admin.site.register(MealPlanMenu, MealPlanMenuAdmin)


class UserMealPlanAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'meal_plan')
    list_display_links = ('user', 'meal_plan')
    list_filter = ('meal_plan',)

    class Meta:
        model = UserMealPlan

admin.site.register(UserMealPlan, UserMealPlanAdmin)
