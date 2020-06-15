from django.shortcuts import render
from django.http import Http404

from .models import Item, Category, Room


def items_overview(request):
    items = Item.objects.all().order_by('name')
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


def get_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404
    context = {
        'item': item
    }
    return render(request, 'item.html', context)


def categories_overview(request):
    categories = Category.objects.all().order_by('name')
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)


def get_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Item.DoesNotExist:
        raise Http404
    context = {
        'category': category
    }
    return render(request, 'category.html', context)


def rooms_overview(request):
    rooms = Room.objects.all().order_by('name')
    context = {
        'rooms': rooms
    }
    return render(request, 'rooms.html', context)


def get_room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except Item.DoesNotExist:
        raise Http404
    context = {
        'room': room
    }
    return render(request, 'room.html', context)
