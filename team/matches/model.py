from django.db import models


class Match(models.Model):
    MATCH_TYPE_CHOICES = (
        (1, 'scrim'),
        (2, 'match'),
    )
    match_type = models.PositiveSmallIntegerField(choices=MATCH_TYPE_CHOICES)
    team_a = models.OneToOneField(
        'Roster', to_field='id', related_name='team_a_id', on_delete=models.CASCADE, unique=True)
    team_b = models.OneToOneField(
        'Roster', to_field='id', related_name='team_b_id', on_delete=models.CASCADE, unique=True)
    event_id = models.OneToOneField(
        to='Event', to_field='id', related_name='event_id', on_delete=models.CASCADE, unique=True)
