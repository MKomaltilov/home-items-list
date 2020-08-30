from django.shortcuts import render
from django.http import Http404

from ..services.items import get_all_items, get_count_of_items, get_item_by_primary_key, get_items_with_filter


def items_overview(request):
    items = get_all_items()
    context = {
        'items': items,
        **get_count_of_items()
    }
    return render(request, 'items/overview.html', context)


def get_item(request, item_id):
    item = get_item_by_primary_key(item_id)
    context = {
        'item': item
    }
    return render(request, 'items/item.html', context)


def items_wo_category(request):
    items = get_items_with_filter(categories=None)
    context = {
        'items': items,
        **get_count_of_items()
    }
    return render(request, 'items/items_wo_category.html', context)


def items_wo_owner(request):
    items = get_items_with_filter(owner=None)
    context = {
        'items': items,
        **get_count_of_items()
    }
    return render(request, 'items/items_wo_owner.html', context)


def items_wo_room(request):
    items = get_items_with_filter(room=None)
    context = {
        'items': items,
        **get_count_of_items()
    }
    return render(request, 'items/items_wo_room.html', context)
