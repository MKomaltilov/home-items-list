from django.urls import path
from home_items.views import items, categories, rooms, users


urlpatterns = [
    path('', items.items_overview, name='items'),
    path('items/<int:item_id>', items.get_item, name='item'),
    path('items/no-category', items.items_wo_category, name='items_wo_category'),
    path('categories/', categories.categories_overview, name='categories'),
    path('categories/<int:category_id>', categories.get_category, name='category'),
    path('rooms/', rooms.rooms_overview, name='rooms'),
    path('rooms/<int:room_id>', rooms.get_room, name='room'),
    path('rooms/no-room', items.items_wo_room, name='items_wo_room'),
    path('users/', users.users_overview, name='users'),
    path('users/<int:user_id>', users.get_user, name='user'),
    path('users/family/', items.items_wo_owner, name='family_items')
]