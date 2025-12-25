from django.test import TestCase
from octofit_tracker.models import Workout


class WorkoutTestCase(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Hero HIIT',
            description='High intensity for heroes'
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Hero HIIT')
        self.assertEqual(self.workout.description, 'High intensity for heroes')

    def test_workout_string_representation(self):
        self.assertEqual(str(self.workout), 'Hero HIIT')
