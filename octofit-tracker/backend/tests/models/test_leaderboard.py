from django.test import TestCase
from octofit_tracker.models import Team, User, Leaderboard


class LeaderboardTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='DC')
        self.user = User.objects.create(
            name='Batman',
            email='batman@dc.com',
            team=self.team
        )
        self.leaderboard = Leaderboard.objects.create(
            user=self.user,
            score=100
        )

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)
        self.assertEqual(self.leaderboard.user.name, 'Batman')

    def test_leaderboard_string_representation(self):
        self.assertEqual(str(self.leaderboard), 'Batman: 100')

    def test_leaderboard_score_update(self):
        self.leaderboard.score = 150
        self.leaderboard.save()
        updated_leaderboard = Leaderboard.objects.get(pk=self.leaderboard.pk)
        self.assertEqual(updated_leaderboard.score, 150)
