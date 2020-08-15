from django.shortcuts import render
from django.http import Http404

from home_items.models import Item, Room


def rooms_overview(request):
    rooms = Room.objects.all().order_by('name')
    context = {
        'rooms': rooms,
        'items_wo_room_count': Item.objects.filter(room=None).count()
    }
    return render(request, 'rooms.html', context)


def get_room(request, room_id):
    try:
        room = Room.objects.prefetch_related('items').get(pk=room_id)
    except Room.DoesNotExist:
        raise Http404
    context = {
        'room': room
    }
    return render(request, 'room.html', context)
