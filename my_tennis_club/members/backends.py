# members/backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from .models import Member

User = get_user_model()

class MemberBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            member = User.objects.get(email=email)
            if member.check_password(password):
                return member
        except User.DoesNotExist:
            return None

