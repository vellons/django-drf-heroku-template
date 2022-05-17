from django.core.validators import MinLengthValidator
from django.db import models

from users.validators import MyUsernameValidator

PROFILE_TYPE_CHOICES = [
    ('STD', 'Standard'),
    ('ADM', 'Admin')
]


class Profile(models.Model):
    username = models.CharField(
        max_length=32,
        unique=True,
        help_text=(
            'Required. 32 characters or fewer. Lowercase letters, digits _ only; must start with a letter.'
        ),
        validators=[MinLengthValidator(4), MyUsernameValidator()],
        error_messages={
            'unique': 'A user with that username already exists.',
        },
    )
    name = models.CharField(max_length=64, null=True)
    surname = models.CharField(max_length=64, null=True)
    type = models.CharField(max_length=3, choices=PROFILE_TYPE_CHOICES, default='STD')
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return '<Profile {} {}>'.format(self.id, self.username)

    def __str__(self):
        return '@{}'.format(self.username)
