from django.contrib import admin
from .models import Room, Category, Item


admin.site.register(Room)
admin.site.register(Category)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
