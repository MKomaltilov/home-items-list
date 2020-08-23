from django.test import TestCase
from django.contrib.auth import get_user_model

from home_items.models import Item, ItemList


User = get_user_model()


class ItemsViewTest(TestCase):
    def test_items_overview_show_list_of_items(self):
        owner = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=owner)
        Item.objects.create(name='first test item', list=item_list)
        Item.objects.create(name='second test item', list=item_list)
        response = self.client.get('/')

        self.assertContains(response, 'first test item')
        self.assertContains(response, 'second test item')
