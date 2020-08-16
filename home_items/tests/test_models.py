from django.test import TestCase
from django.contrib.auth import get_user_model
from home_items.models import Room, Category, Item, ItemList

User = get_user_model()


class RoomModelTest(TestCase):
    def test_default_room_with_blank_description_can_be_created(self):
        owner = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=owner)
        room = Room.objects.create(name='test name', list=item_list)

        self.assertEqual(room.name, 'test name')
        self.assertIsNone(room.description)

    def test_room_with_name_and_description_can_be_created(self):
        owner = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=owner)
        room = Room.objects.create(name='test name', description='test description', list=item_list)

        self.assertEqual(room.name, 'test name')
        self.assertEqual(room.description, 'test description')


class CategoryModelTest(TestCase):
    def test_default_category_with_blank_description_can_be_created(self):
        owner = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=owner)
        category = Category.objects.create(name='test name', list=item_list)

        self.assertEqual(category.name, 'test name')
        self.assertIsNone(category.description)

    def test_category_with_name_and_description_can_be_created(self):
        owner = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=owner)
        category = Category.objects.create(name='test name', description='test description', list=item_list)

        self.assertEqual(category.name, 'test name')
        self.assertEqual(category.description, 'test description')


class ItemModelTest(TestCase):
    def test_default_item_can_be_created(self):
        owner = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=owner)
        item = Item.objects.create(name='test item', list=item_list)

        self.assertEqual(item.name, 'test item')
        self.assertIsNone(item.description)
        self.assertIsNone(item.owner)
        self.assertIsNone(item.room)
        self.assertEqual(len(item.categories.all()), 0)

    def test_room_user_and_categories_can_be_added_to_item(self):
        owner = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=owner)

        category_one = Category.objects.create(name='category 1', list=item_list)
        category_two = Category.objects.create(name='category 2', list=item_list)
        category_three = Category.objects.create(name='category 3', list=item_list)

        room = Room.objects.create(name='test name', list=item_list)

        item = Item.objects.create(
            name='test item',
            description='some text in description',
            owner=owner,
            room=room,
            list=item_list
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


class ItemsListModelTest(TestCase):
    def test_list_with_default_parameters_can_be_created(self):
        owner = User.objects.create(username='user', password='123')
        item_list = ItemList.objects.create(name='test list', owner=owner)

        self.assertEqual(item_list.name, 'test list')
        self.assertEqual(item_list.owner.username, 'user')
        self.assertIsNone(item_list.description)
        self.assertEqual(len(item_list.editors.all()), 0)
