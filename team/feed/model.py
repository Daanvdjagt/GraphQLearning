from django.db import models


class Feed(models.Model):
    feedItem = models.ManyToManyField('FeedItem', blank=True)


class FeedItem(models.Model):
    FEEDITEM_TYPE_CHOICES = (
        (1, 'message'),
        (2, 'twitter'),
        (3, 'youtube'),
    )
    item_name = models.CharField(max_length=255)
    item_type = models.PositiveIntegerField(choices=FEEDITEM_TYPE_CHOICES)
    item_body = models.CharField(max_length=255)
