from django.urls import path
from . import views


urlpatterns = [
    path('', views.items_overview, name='items'),
    path('items/<int:item_id>', views.get_item, name='get_item')
]