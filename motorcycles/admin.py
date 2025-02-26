from django.contrib import admin
from motorcycles.models import Motorcycle


class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

admin.site.register(Motorcycle, MotorcycleAdmin)