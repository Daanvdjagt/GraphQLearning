from django.db import models


class Roster(models.Model):
    players = models.ManyToManyField('Player', blank=True)
    feed_id = models.OneToOneField(
        to='Feed', to_field='id', related_name='feed_id', on_delete=models.CASCADE)


class PlayerRole(models.Model):
    player_role = models.CharField(max_length=20, primary_key=True)


class Player(models.Model):
    player_role = models.ForeignKey(
        to='PlayerRole', to_field='player_role', on_delete=models.CASCADE)
    player_name = models.CharField(max_length=255)
