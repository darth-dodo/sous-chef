# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User

from mealplans.models import MealPlan, MealPlanMenu, UserMealPlan


class MealPlanMenuInline(admin.TabularInline):
    model = MealPlanMenu


class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'description')
    search_fields = ['name']
    list_editable = ['name']

    inlines = [MealPlanMenuInline]

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
    list_display_links = ('__str__', 'user', 'meal_plan')
    list_filter = ('meal_plan',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user' and not request.user.is_superuser:
            kwargs['initial'] = request.user.id
            kwargs['queryset'] = User.objects.filter(id=request.user.id)
            return db_field.formfield(**kwargs)

        return super(UserMealPlanAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Meta:
        model = UserMealPlan

admin.site.register(UserMealPlan, UserMealPlanAdmin)
