from django.contrib import admin
from .models import Room, Category, Item


admin.site.register(Room)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'owner', 'id')
    list_display_links = ('name', 'room', 'owner')
    list_filter = ('categories', 'room', 'owner')
    search_fields = ('name',)
    filter_horizontal = ('categories',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)
