from django.db import models


class Schedule(models.Model):
    event_items = models.ManyToManyField('Event', blank=True)


class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateTimeField()
