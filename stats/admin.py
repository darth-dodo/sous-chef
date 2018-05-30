# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.forms import ModelForm

# Register your models here.
from stats.models import WeightLog, DayVariant

from django.contrib.auth.models import User


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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user' and not request.user.is_superuser:
            kwargs['initial'] = request.user.id
            kwargs['queryset'] = User.objects.filter(id=request.user.id)
            return db_field.formfield(**kwargs)

        return super(WeightLogAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(WeightLog, WeightLogAdmin)


class DayVariantAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'description']
    search_fields = ['name']
    list_display_links = ['__str__']

    class Meta:
        model = DayVariant

admin.site.register(DayVariant, DayVariantAdmin)
