from django.shortcuts import render
from .models import Item


def index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)
