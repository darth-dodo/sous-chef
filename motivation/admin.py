# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User

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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'created_by':
            kwargs['initial'] = request.user.id
            kwargs['queryset'] = User.objects.filter(id=request.user.id)
            return db_field.formfield(**kwargs)

        return super(MotivationRatingAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(MotivationRating, MotivationRatingAdmin)


class MotivationalStuffAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_url', 'category', 'rating', 'created_by')
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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'created_by' and not request.user.is_superuser:
            kwargs['initial'] = request.user.id
            kwargs['queryset'] = User.objects.filter(id=request.user.id)
            return db_field.formfield(**kwargs)

        return super(MotivationalStuffAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(MotivationalStuff, MotivationalStuffAdmin)


