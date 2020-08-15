from django.test import TestCase
from django.contrib.auth import get_user_model
from home_items.models import Room, Category, Item

User = get_user_model()


class RoomModelTest(TestCase):
    def test_default_room_with_blank_description_can_be_created(self):
        room = Room.objects.create(name='test name')
        self.assertEqual(room.name, 'test name')
        self.assertEqual(room.description, None)

    def test_room_with_name_and_description_can_be_created(self):
        room = Room.objects.create(name='test name', description='test description')
        self.assertEqual(room.name, 'test name')
        self.assertEqual(room.description, 'test description')


class CategoryModelTest(TestCase):
    def test_default_category_with_blank_description_can_be_created(self):
        category = Category.objects.create(name='test name')
        self.assertEqual(category.name, 'test name')
        self.assertEqual(category.description, None)

    def test_category_with_name_and_description_can_be_created(self):
        category = Category.objects.create(name='test name', description='test description')
        self.assertEqual(category.name, 'test name')
        self.assertEqual(category.description, 'test description')


class ItemModelTest(TestCase):
    def test_default_item_can_be_created(self):
        item = Item.objects.create(name='test item')
        self.assertEqual(item.name, 'test item')
        self.assertEqual(item.description, None)
        self.assertEqual(item.owner, None)
        self.assertEqual(item.room, None)
        self.assertEqual(len(item.categories.all()), 0)

    def test_room_user_and_categories_can_be_added_to_item(self):
        category_one = Category.objects.create(name='category 1')
        category_two = Category.objects.create(name='category 2')
        category_three = Category.objects.create(name='category 3')
        room = Room.objects.create(name='test name')
        owner = User.objects.create(username='user', password='123')

        item = Item.objects.create(
            name='test item',
            description='some text in description',
            owner=owner,
            room=room,
        )
        item.categories.set([category_one, category_three])
        item.save()

        self.assertEqual(item.name, 'test item')
        self.assertEqual(item.description, 'some text in description')
        self.assertEqual(item.owner.username, 'user')
        self.assertEqual(item.room.name, 'test name')
        self.assertIn(category_one, item.categories.all())
        self.assertIn(category_three, item.categories.all())
        self.assertNotIn(category_two, item.categories.all())
