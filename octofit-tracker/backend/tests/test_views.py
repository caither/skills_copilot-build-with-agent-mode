from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

class APIRootTestCase(APITestCase):
    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('leaderboards', response.data)

class TeamViewSetTestCase(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')

    def test_list_teams(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Marvel')

    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'DC'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)

class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=self.team)

    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Iron Man')

    def test_create_user(self):
        url = reverse('user-list')
        data = {'name': 'Captain America', 'email': 'cap@marvel.com', 'team_id': self.team.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

class ActivityViewSetTestCase(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=30)

    def test_list_activities(self):
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['type'], 'Run')

    def test_create_activity(self):
        url = reverse('activity-list')
        data = {'user_id': self.user.id, 'type': 'Swim', 'duration': 45}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 2)

class WorkoutViewSetTestCase(APITestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')

    def test_list_workouts(self):
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Hero HIIT')

    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Power Lift', 'description': 'Strength for superhumans'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 2)

class LeaderboardViewSetTestCase(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=self.team)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_list_leaderboards(self):
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['score'], 100)

    def test_create_leaderboard(self):
        url = reverse('leaderboard-list')
        data = {'user_id': self.user.id, 'score': 200}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Leaderboard.objects.count(), 2)
