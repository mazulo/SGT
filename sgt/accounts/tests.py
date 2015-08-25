from django.test import TestCase
from django.contrib.auth import get_user_model
from . import models


class TestUser(TestCase):

    User = get_user_model()

    def test_creation(self):
        user = self.User.objects.create(
            username='desbravador', email='dbv@dbv.com',
        )
        self.assertIsInstance(user, models.UserDbv)
