from django.shortcuts import render
from django.http import Http404

from home_items.models import Item


def items_wo_room(request):
    items = Item.objects\
        .prefetch_related('categories')\
        .select_related('room')\
        .select_related('owner')\
        .filter(room=None)\
        .order_by('name')
    context = {
        'items': items,
        'items_count': Item.objects.all().count(),
        'family_items_count': Item.objects.filter(owner=None).count(),
        'items_wo_category_count': Item.objects.filter(categories=None).count(),
        'items_wo_room_count': Item.objects.filter(room=None).count()
    }
    return render(request, 'items/items_wo_room.html', context)


def items_overview(request):
    items = Item.objects\
        .prefetch_related('categories')\
        .select_related('room')\
        .select_related('owner')\
        .all()\
        .order_by('name')
    context = {
        'items': items,
        'items_count': Item.objects.all().count(),
        'family_items_count': Item.objects.filter(owner=None).count(),
        'items_wo_category_count': Item.objects.filter(categories=None).count(),
        'items_wo_room_count': Item.objects.filter(room=None).count()
    }
    return render(request, 'items/index.html', context)


def get_item(request, item_id):
    try:
        item = Item.objects\
            .prefetch_related('categories') \
            .select_related('room') \
            .select_related('owner') \
            .get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404
    context = {
        'item': item
    }
    return render(request, 'items/item.html', context)


def items_wo_category(request):
    items = Item.objects\
        .prefetch_related('categories')\
        .select_related('room')\
        .select_related('owner')\
        .filter(categories=None)\
        .order_by('name')
    context = {
        'items': items,
        'items_count': Item.objects.all().count(),
        'family_items_count': Item.objects.filter(owner=None).count(),
        'items_wo_category_count': Item.objects.filter(categories=None).count(),
        'items_wo_room_count': Item.objects.filter(room=None).count()
    }
    return render(request, 'items/items_wo_category.html', context)


def family_items(request):
    items = Item.objects\
        .prefetch_related('categories')\
        .select_related('room')\
        .select_related('owner')\
        .filter(owner=None)\
        .order_by('name')
    context = {
        'items': items,
        'items_count': Item.objects.all().count(),
        'family_items_count': Item.objects.filter(owner=None).count(),
        'items_wo_category_count': Item.objects.filter(categories=None).count(),
        'items_wo_room_count': Item.objects.filter(room=None).count()
    }
    return render(request, 'items/family_items.html', context)

