import firebase_admin
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication

from myapp import settings
from .exceptions import FirebaseError
from .exceptions import InvalidAuthToken
from .exceptions import NoAuthToken

credential = credentials.Certificate(settings.FIREBASE_CREDENTIAL)
default_app = firebase_admin.initialize_app(credential)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            raise NoAuthToken()

        id_token = auth_header.split(' ').pop()
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken()
            pass

        if not id_token or not decoded_token:
            return None
        # print('decoded_token {}'.format(decoded_token))

        try:
            uid = decoded_token.get('uid')
            email = decoded_token.get('email')
            sign_in_provider = decoded_token.get('firebase')['sign_in_provider']
        except Exception:
            raise FirebaseError()

        user, created = User.objects.get_or_create(username=uid)
        user.email = email
        user.last_login = timezone.localtime()
        user.profile.sign_in_provider = sign_in_provider
        if created:
            user.profile.username = uid
        user.save()

        return user, created
