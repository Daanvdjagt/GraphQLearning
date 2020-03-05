from django.db import models


class MatchType(models.Model):
    match_type = models.CharField(max_length=20, primary_key=True)


class Match(models.Model):
    match_type = models.ForeignKey(
        to='MatchType', to_field='match_type', on_delete=models.CASCADE)
    roster = models.ForeignKey(
        to='Roster', to_field='id', related_name='roster_id', on_delete=models.CASCADE)
    enemy_team_name = models.CharField(max_length=50)
    event_id = models.OneToOneField(
        to='Event', to_field='id', related_name='event_id', on_delete=models.CASCADE, unique=True)
