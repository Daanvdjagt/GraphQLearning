from django.contrib import admin
from .models import *


class FeedItemAdmin(admin.ModelAdmin):
    fields = ('item_name', 'item_type', 'item_body',)


class FeedAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    fields = ('event_name', 'event_date',)


class ScheduleAdmin(admin.ModelAdmin):
    pass


class MatchAdmin(admin.ModelAdmin):
    fields = ('match_type', 'roster', 'enemy_team_name', 'event_id',)


class RosterAdmin(admin.ModelAdmin):
    fields = ('feed_id', 'players')


class PlayerAdmin(admin.ModelAdmin):
    fields = ('player_role', 'player_name')


class PlayerRoleAdmin(admin.ModelAdmin):
    field = ('player_role')


class TeamAdmin(admin.ModelAdmin):
    field = ('team_name', 'roster_id',)


class MatchTypeAdmin(admin.ModelAdmin):
    field = ('match_type')


admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedItem, FeedItemAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Roster, RosterAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerRole, PlayerRoleAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(MatchType, MatchTypeAdmin)
