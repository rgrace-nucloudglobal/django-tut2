from django.contrib import admin

from Things.models import Thing, Color, Shape

# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    fields = ['enName', 'description']

class ShapeAdmin(admin.ModelAdmin):
    fields = ['enName', 'description']

class ThingAdmin(admin.ModelAdmin):
    fields = ['enName', 'color', 'shape', 'description']


admin.site.register(Color, ColorAdmin)
admin.site.register(Shape, ShapeAdmin)
admin.site.register(Thing, ThingAdmin)
