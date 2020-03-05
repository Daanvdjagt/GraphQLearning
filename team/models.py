
from team.feed.model import *
from team.roster.model import *
from team.schedule.model import *
from team.matches.model import *


from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    roster_id = models.OneToOneField(
        to='Roster', to_field='id', on_delete=models.CASCADE)
