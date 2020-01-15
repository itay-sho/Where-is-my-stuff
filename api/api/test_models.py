import random
from django.test import TestCase
from django.contrib.auth.models import User

from api.api.models import *


class PersonTestCase(TestCase):
    @staticmethod
    def create_person(username, email=None, password=None):
        user = User.objects.create_user(username, email, password)
        person = Person.objects.create(user_id=user.id)

        return person, user

    def setUp(self):
        self.person, self.user = type(self).create_person('random_user1')

    def test_removing_user__person_removed(self):
        assert len(Person.objects.filter(id=self.person.id)) == 1

        # deleting user, expecting person to be removed as well
        # using filter and not get, in order to be sure that it works with delete of queryset
        User.objects.filter(id=self.user.id).delete()

        assert len(Person.objects.filter(id=self.person.id)) == 0

    def test_removing_person__user_removed(self):
        assert len(User.objects.filter(id=self.user.id)) == 1

        # deleting person, expecting user to be removed as well
        # using filter and not get, in order to be sure that it works with delete of queryset
        Person.objects.filter(id=self.person.id).delete()

        assert len(User.objects.filter(id=self.user.id)) == 0


class ItemTestCase(TestCase):
    def setUp(self):
        self.person, _ = PersonTestCase.create_person('random_user3')
        self.item = type(self).create_item('a', self.person)

    @staticmethod
    def create_item(name, person, current_location=None):
        item = Item.objects.create(
            name=name,
            person_id=person.id,
            current_location=current_location
        )

        return item

    def test_creating_item_no_location__item_creates(self):
        assert type(self).create_item('1', self.person, current_location=None)

    def test_creating_item_with_location__item_creates(self):
        location = LocationTestCase.create_location('b', self.person)
        assert type(self).create_item('1', self.person, current_location=location)

    def test_removing_person__items_removed(self):
        type(self).create_item('b', self.person)
        type(self).create_item('c', self.person)
        type(self).create_item('d', self.person)
        type(self).create_item('e', self.person)

        assert len(Item.objects.filter(person_id=self.person.id)) == 5

        # deleting person, expecting items to be removed as well
        # using filter and not get, in order to be sure that it works with delete of queryset
        Person.objects.filter(id=self.person.id).delete()

        assert len(Item.objects.filter(person_id=self.person.id)) == 0


class LocationTestCase(TestCase):
    @staticmethod
    def create_location(name, person, description=''):
        return Location.objects.create(name=name, person_id=person.id, description=description)


class EventTestCase(TestCase):
    pass
