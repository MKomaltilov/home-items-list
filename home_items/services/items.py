from home_items.models import Item


def get_all_items():
    items = Item.objects \
        .prefetch_related('categories') \
        .select_related('room') \
        .select_related('owner') \
        .all() \
        .order_by('name')
    return items
