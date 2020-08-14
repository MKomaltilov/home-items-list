from django.test import TestCase
from django.contrib import auth
from home_items.models import Room, Category, Item

User = auth.get_user_model()


class RoomModelTest(TestCase):
    def test_default_room_with_blank_description_can_be_created(self):
        room = Room.objects.create(name='test name')
        self.assertEqual(room.name, 'test name')
        self.assertEqual(room.description, None)


class CategoryModelTest(TestCase):
    def test_default_category_with_blank_description_can_be_created(self):
        room = Category.objects.create(name='test name')
        self.assertEqual(room.name, 'test name')
        self.assertEqual(room.description, None)


class ItemModelTest(TestCase):
    def test_default_item_can_be_created(self):
        item = Item.objects.create(name='test item')
        self.assertEqual(item.name, 'test item')
        self.assertEqual(item.description, None)
        self.assertEqual(item.owner, None)
        self.assertEqual(item.room, None)
        # self.assertIn(None, item.categories.all())
        print(item.categories.all())
