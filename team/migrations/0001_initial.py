# Generated by Django 3.0.3 on 2020-03-05 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('item_type', models.PositiveIntegerField(choices=[(1, 'message'), (2, 'twitter'), (3, 'youtube')])),
                ('item_body', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MatchType',
            fields=[
                ('match_type', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerRole',
            fields=[
                ('player_role', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='feed_id', to='team.Feed')),
                ('players', models.ManyToManyField(blank=True, to='team.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('roster_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.Roster')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_items', models.ManyToManyField(blank=True, to='team.Event')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='player_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.PlayerRole'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enemy_team_name', models.CharField(max_length=50)),
                ('event_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='event_id', to='team.Event')),
                ('match_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.MatchType')),
                ('roster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roster_id', to='team.Roster')),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='feedItem',
            field=models.ManyToManyField(blank=True, to='team.FeedItem'),
        ),
    ]