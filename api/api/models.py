from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    class Meta:
        # fixing plural in django admin
        verbose_name_plural = "People"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')

    def set_current_location(self, location):
        self.current_location = location


class Item(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)

    def set_current_location(self, location):
        self.current_location = location

    def __str__(self):
        return f'{self.name} in {self.current_location.name if self.current_location else "Unassigned"}'


class Location(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='locations')
    current_user = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='current_location', null=True)
    current_items = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='current_location', null=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name


class Event(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    name = models.CharField(max_length=100)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
    # TODO: consider changing begin and end date with duration, and add a EventOccurrence model