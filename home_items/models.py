import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    list = models.ForeignKey('ItemList', on_delete=models.CASCADE, related_name='rooms')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    list = models.ForeignKey('ItemList', on_delete=models.CASCADE, related_name='categories')
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    list = models.ForeignKey('ItemList', on_delete=models.CASCADE, related_name='items')
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='items')
    categories = models.ManyToManyField('Category', blank=True, related_name='items')
    room = models.ForeignKey('Room', null=True, blank=True, on_delete=models.SET_NULL, related_name='items')

    def __str__(self):
        return self.name


class ItemList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item_lists')
    editors = models.ManyToManyField(User, related_name='shared_lists', blank=True)

    def __str__(self):
        return self.name
