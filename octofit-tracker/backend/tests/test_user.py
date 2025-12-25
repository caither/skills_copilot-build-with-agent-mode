from django.test import TestCase
from octofit_tracker.models import Team, User


class UserTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(
            name='Iron Man',
            email='ironman@marvel.com',
            team=self.team
        )

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Iron Man')
        self.assertEqual(self.user.email, 'ironman@marvel.com')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_user_unique_email(self):
        with self.assertRaises(Exception):
            User.objects.create(
                name='Another Hero',
                email='ironman@marvel.com',
                team=self.team
            )

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), 'Iron Man')
