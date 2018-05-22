# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from recipes.models import Recipe, Ingredient, NutritionalInformation


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'availability', 'low_shelf_life')
    search_fields = ['name']
    list_filter = ['availability', 'low_shelf_life']
    list_editable = ['availability']

    class Meta:
        model = Ingredient


admin.site.register(Ingredient, IngredientAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'difficulty', 'created_at', 'original_url')
    search_fields = ['name', 'url']
    list_filter = ['category', 'difficulty', 'is_veg', 'servings']
    list_editable = ['category', 'difficulty']

    class Meta:
        model = Recipe

    def original_url(self, obj):
        if  obj.url:
            return '<a href="{0}" target="_blank" >{0}</a>'.format(obj.url)
        else:
            return ''

    original_url.allow_tags = True
    original_url.short_description = 'Recipe URL'


admin.site.register(Recipe, RecipeAdmin)


class NutritionalInformationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'net_carbs', 'carbs', 'fats',
                    'protein', 'fibre']
    list_select_related = ['recipe']

    class Meta:
        model = NutritionalInformation

admin.site.register(NutritionalInformation, NutritionalInformationAdmin)
