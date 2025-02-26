from django.contrib import admin
from motorcycles.models import Motorcycle, Brand


class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Motorcycle, MotorcycleAdmin)
admin.site.register(Brand, BrandAdmin)