from home_items.models import Item


def get_all_items():
    items = Item.objects \
        .prefetch_related('categories') \
        .select_related('room') \
        .select_related('owner') \
        .all() \
        .order_by('name')
    return items


def get_count_of_items():
    return {
        'items_count': Item.objects.all().count(),
        'family_items_count': Item.objects.filter(owner=None).count(),
        'items_wo_category_count': Item.objects.filter(categories=None).count(),
        'items_wo_room_count': Item.objects.filter(room=None).count()
    }


def create_item(name, item_list):
    return Item.objects.create(name=name, list=item_list)
