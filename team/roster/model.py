from django.db import models


class Roster(models.Model):
    roster_name = models.CharField(max_length=50)
    players = models.ManyToManyField('Player', blank=True)


class PlayerRole(models.Model):
    player_role = models.CharField(max_length=20, primary_key=True)


class Player(models.Model):
    player_role = models.ForeignKey(
        to='PlayerRole', to_field='player_role', on_delete=models.CASCADE)
    player_name = models.CharField(max_length=255)
    roster_id = models.ForeignKey(
        to='Roster', to_field='id', related_name='roster_id', on_delete=models.CASCADE)
