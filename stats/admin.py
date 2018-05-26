# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.forms import ModelForm

# Register your models here.
from stats.models import WeightLog, DayVariant


# class WeightLogAdminForm(ModelForm):
#     def clean_user:
#         if not request.user.is_superuser:
#

# TODO validation for user and request user

class WeightLogAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'day_variant', 'calories_consumed'
                    , 'weight', 'my_fitness_plan_entry')
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    list_filter = ['day_variant']
    list_display_links = ['__str__', 'day_variant']

    class Meta:
        model = WeightLog

    def get_queryset(self, request):
        qs = super(WeightLogAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)

        return qs

admin.site.register(WeightLog, WeightLogAdmin)


class DayVariantAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'description']
    search_fields = ['name']
    list_display_links = ['__str__']

    class Meta:
        model = DayVariant

admin.site.register(DayVariant, DayVariantAdmin)
