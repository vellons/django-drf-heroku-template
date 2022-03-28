from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

PROFILE_TYPE_CHOICES = [
    ('STD', 'Standard'),
    ('ADM', 'Admin')
]


class Profile(models.Model):
    id = models.CharField(max_length=32, primary_key=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    username = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, null=True)
    lastname = models.CharField(max_length=64, null=True)
    type = models.CharField(max_length=3, choices=PROFILE_TYPE_CHOICES, default='STD')
    is_verified = models.BooleanField(default=False)
    bio = models.TextField(max_length=512, null=True)
    sign_in_provider = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return '<Profile {} {}>'.format(self.id, self.username)

    def __str__(self):
        return '@{}'.format(self.id)


@receiver(post_save, sender=User)  # Received from firebase_auth
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(id=instance.username, user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
