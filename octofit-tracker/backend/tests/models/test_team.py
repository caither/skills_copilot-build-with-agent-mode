from django.test import TestCase
from octofit_tracker.models import Team


class TeamTestCase(TestCase):
    def setUp(self):
        self.team_marvel = Team.objects.create(name='Marvel')
        self.team_dc = Team.objects.create(name='DC')

    def test_team_creation(self):
        self.assertEqual(self.team_marvel.name, 'Marvel')
        self.assertEqual(self.team_dc.name, 'DC')

    def test_team_unique_name(self):
        with self.assertRaises(Exception):
            Team.objects.create(name='Marvel')

    def test_team_string_representation(self):
        self.assertEqual(str(self.team_marvel), 'Marvel')
