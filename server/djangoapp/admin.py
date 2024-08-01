from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
class CarModelInline(admin.StackedInline):
    model = CarModel

class CarModelAdmin(admin.ModelAdmin):
    fields = ('name',)

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    fields = ('name',)
    
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
