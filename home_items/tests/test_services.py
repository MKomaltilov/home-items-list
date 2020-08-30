from django.test import TestCase
from django.contrib.auth import get_user_model
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist

import uuid

from home_items.models import Item, ItemList
from home_items.services.items import get_all_items, get_count_of_items, create_item, get_item_by_primary_key, get_items_with_filter

User = get_user_model()


class ItemsServiceTest(TestCase):
    def test_get_item_by_primary_key_returns_right_item(self):
        items = self._create_items(amount=1)
        item = get_item_by_primary_key(items[0].id)
        self.assertEqual(items[0], item)

    def test_get_item_by_primary_key_with_not_existing_uuid_returns_Http404(self):
        self._create_items(amount=1)
        item = get_item_by_primary_key(uuid.uuid4())
        self.assertEqual(item, Http404)

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

        item_list = self._create_list()
        item = create_item('item one', item_list)

        items = get_all_items()
        self.assertEqual(len(items), 1)
        self.assertIn(item, items)

    def test_get_items_with_filter_return_right_items(self):
        self._create_items(amount=3, owner=True)
        self._create_items(amount=5)

        items_wo_owner = get_items_with_filter(owner=None)
        items_wo_room = get_items_with_filter(room=None)

        self.assertEqual(len(items_wo_owner), 5)
        self.assertEqual(len(items_wo_room), 8)

    def _create_items(self, amount=1, owner=False):
        user = self._create_user()
        item_list = self._create_list(owner=user)
        items = []
        for i in range(amount):
            if owner:
                items.append(Item.objects.create(name=f'test item {i}', list=item_list, owner=user))
            else:
                items.append(Item.objects.create(name=f'test item {i}', list=item_list))
        return items

    def _create_list(self, owner=None):
        if owner is None:
            return ItemList.objects.create(name='test list', owner=self._create_user())
        else:
            return ItemList.objects.create(name='test list', owner=owner)

    def _create_user(self):
        try:
            return User.objects.get(username='user')
        except ObjectDoesNotExist:
            return User.objects.create(username='user', password='123')
