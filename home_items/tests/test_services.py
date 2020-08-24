from django.test import TestCase
from django.contrib.auth import get_user_model

from home_items.models import Item, ItemList
from home_items.services.items import get_all_items, get_count_of_items, create_item

User = get_user_model()


class ItemsServiceTest(TestCase):
    def test_get_all_items_returns_zero_items_without_items(self):
        items = get_all_items()
        self.assertEqual(len(items), 0)

    def test_get_all_items_returns_all_items(self):
        self._create_items(amount=3)
        items = get_all_items()
        self.assertEqual(len(items), 3)

    def test_get_count_of_items_returns_zeroes_without_items(self):
        for term, count in get_count_of_items().items():
            self.assertEqual(count, 0)

    def test_get_count_of_items_returns_right_counts(self):
        self._create_items(amount=5, owner=True)
        count_of_items = get_count_of_items()

        self.assertEqual(count_of_items['items_count'], 5)
        self.assertEqual(count_of_items['family_items_count'], 0)
        self.assertEqual(count_of_items['items_wo_category_count'], 5)
        self.assertEqual(count_of_items['items_wo_room_count'], 5)

    def test_create_item_returns_created_item(self):
        items = get_all_items()
        self.assertEqual(len(items), 0)

        user = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=user)
        item = create_item('item one', item_list)

        items = get_all_items()
        self.assertEqual(len(items), 1)
        self.assertIn(item, items)

    def _create_items(self, amount=1, owner=False):
        user = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=user)
        for i in range(amount):
            if owner:
                Item.objects.create(name=f'test item {i}', list=item_list, owner=user)
            else:
                Item.objects.create(name=f'test item {i}', list=item_list)
