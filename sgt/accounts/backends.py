from django.conf import settings
from django.contrib.auth.models import check_password
from .models import UserDbv


class EmailAuthBackend(object):
    """
    A custom authentication backend.
        Allows users to log in using their email address.
    """

    def authenticate(self, email=None, password=None):
        """
        Authentication method
        """
        try:
            user = UserDbv.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserDbv.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserDbv.objects.get(pk=user_id)
        except UserDbv.DoesNotExist:
            return None
