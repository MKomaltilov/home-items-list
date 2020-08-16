from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from home_items.models import Item


def users_overview(request):
    users = User.objects.all()
    context = {
        'users': users,
        'family_items_count': Item.objects.filter(owner=None).count()
    }
    return render(request, 'users/overview.html', context)


def get_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404
    context = {
        'user': user
    }
    return render(request, 'users/user.html', context)