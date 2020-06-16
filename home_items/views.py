from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from .models import Item, Category, Room


def items_overview(request):
    items = Item.objects.all().order_by('name')
    context = {
        'items': items,
        'family_items_count': Item.objects.filter(owner=None).count(),
        'items_wo_category_count': Item.objects.filter(categories=None).count(),
        'items_wo_room_count': Item.objects.filter(room=None).count()
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


def items_wo_category(request):
    items = Item.objects.filter(categories=None).order_by('name')
    context = {
        'items': items,
        'family_items_count': Item.objects.filter(owner=None).count(),
        'items_wo_category_count': Item.objects.filter(categories=None).count(),
        'items_wo_room_count': Item.objects.filter(room=None).count()
    }
    return render(request, 'items_wo_category.html', context)


def categories_overview(request):
    categories = Category.objects.all().order_by('name')
    context = {
        'categories': categories,
        'items_wo_category_count': Item.objects.filter(categories=None).count()
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
        'rooms': rooms,
        'items_wo_room_count': Item.objects.filter(room=None).count()
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


def users_overview(request):
    users = User.objects.all()
    context = {
        'users': users,
        'family_items_count': Item.objects.filter(owner=None).count()
    }
    return render(request, 'users.html', context)


def get_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except Item.DoesNotExist:
        raise Http404
    context = {
        'user': user
    }
    return render(request, 'user.html', context)


def family_items(request):
    items = Item.objects.filter(owner=None).order_by('name')
    context = {
        'items': items,
        'family_items_count': Item.objects.filter(owner=None).count(),
        'items_wo_category_count': Item.objects.filter(categories=None).count(),
        'items_wo_room_count': Item.objects.filter(room=None).count()
    }
    return render(request, 'family_items.html', context)


def items_wo_room(request):
    items = Item.objects.filter(room=None).order_by('name')
    context = {
        'items': items,
        'family_items_count': Item.objects.filter(owner=None).count(),
        'items_wo_category_count': Item.objects.filter(categories=None).count(),
        'items_wo_room_count': Item.objects.filter(room=None).count()
    }
    return render(request, 'items_wo_room.html', context)