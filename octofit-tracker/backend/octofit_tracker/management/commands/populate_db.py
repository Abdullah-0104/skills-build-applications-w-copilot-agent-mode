from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        Activity.objects.create(user=captain, type='cycle', duration=45, calories=400)
        Activity.objects.create(user=batman, type='swim', duration=60, calories=500)
        Activity.objects.create(user=superman, type='run', duration=50, calories=600)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=1000)
        Leaderboard.objects.create(user=batman, score=1200)
        Leaderboard.objects.create(user=superman, score=1100)
        Leaderboard.objects.create(user=captain, score=900)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
