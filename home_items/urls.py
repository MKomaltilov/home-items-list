from django.urls import path
from . import views


urlpatterns = [
    path('', views.items_overview, name='items'),
    path('items/<int:item_id>', views.get_item, name='item'),
    path('items/no-category', views.items_wo_category, name='items_wo_category'),
    path('categories/', views.categories_overview, name='categories'),
    path('categories/<int:category_id>', views.get_category, name='category'),
    path('rooms/', views.rooms_overview, name='rooms'),
    path('rooms/<int:room_id>', views.get_room, name='room')
]