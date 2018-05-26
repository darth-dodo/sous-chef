# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from motivation.models import MotivationCategory, MotivationRating, MotivationalStuff


class MotivationCategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'created_by')
    search_fields = ['name']

    class Meta:
        model = MotivationCategory

admin.site.register(MotivationCategory, MotivationCategoryAdmin)


class MotivationRatingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'created_by')
    search_fields = ['name']

    class Meta:
        model = MotivationRating

admin.site.register(MotivationRating, MotivationRatingAdmin)


class MotivationalStuffAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'original_url', 'category', 'rating', 'created_by')
    search_fields = ['name', 'url']
    list_filter = ['category', 'created_by', 'rating']
    list_display_links = ['name']

    class Meta:
        model = MotivationalStuff

    def original_url(self, obj):
        if obj.url:
            return '<a href="{0}" target="_blank" >{0}</a>'.format(obj.url)
        else:
            return 'NA'

    original_url.allow_tags = True
    original_url.short_description = 'URL'

admin.site.register(MotivationalStuff, MotivationalStuffAdmin)


