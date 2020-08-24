from django.shortcuts import render
from django.http import Http404

from home_items.models import Item

from ..services.items import get_all_items, get_count_of_items


def items_overview(request):
    items = get_all_items()
    context = {
        'items': items,
        **get_count_of_items()
    }
    return render(request, 'items/overview.html', context)


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
        **get_count_of_items()
    }
    return render(request, 'items/items_wo_category.html', context)


def items_wo_owner(request):
    items = Item.objects\
        .prefetch_related('categories')\
        .select_related('room')\
        .select_related('owner')\
        .filter(owner=None)\
        .order_by('name')
    context = {
        'items': items,
        **get_count_of_items()
    }
    return render(request, 'items/items_wo_owner.html', context)


def items_wo_room(request):
    items = Item.objects\
        .prefetch_related('categories')\
        .select_related('room')\
        .select_related('owner')\
        .filter(room=None)\
        .order_by('name')
    context = {
        'items': items,
        **get_count_of_items()
    }
    return render(request, 'items/items_wo_room.html', context)
