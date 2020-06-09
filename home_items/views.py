from django.shortcuts import render
from django.http import Http404

from .models import Item


def index(request):
    items = Item.objects.all()
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