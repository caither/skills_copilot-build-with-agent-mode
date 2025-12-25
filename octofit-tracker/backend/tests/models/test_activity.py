from django.test import TestCase
from octofit_tracker.models import Team, User, Activity


class ActivityTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(
            name='Captain America',
            email='cap@marvel.com',
            team=self.team
        )
        self.activity = Activity.objects.create(
            user=self.user,
            type='Run',
            duration=30
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Run')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.user.name, 'Captain America')

    def test_activity_string_representation(self):
        self.assertEqual(str(self.activity), 'Captain America - Run')
