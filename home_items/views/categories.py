from django.shortcuts import render
from django.http import Http404

from home_items.models import Item, Category


def categories_overview(request):
    categories = Category.objects.all().order_by('name')
    context = {
        'categories': categories,
        'items_wo_category_count': Item.objects.filter(categories=None).count()
    }
    return render(request, 'categories.html', context)


def get_category(request, category_id):
    try:
        category = Category.objects.prefetch_related('items').get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404
    context = {
        'category': category
    }
    return render(request, 'category.html', context)