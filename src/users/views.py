from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from firebase_auth.permissions import ProfileOfUser
from users.models import Profile
from users.serializers import ProfileSerializer, ProfileShareSerializer


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all().order_by('created_at')
    serializer_class = ProfileShareSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['username', 'name', 'lastname', 'type', 'is_verified']
    search_fields = ['username', 'name', 'lastname']  # ?search=LIKE in all these fields
    ordering_fields = ['username', 'name', 'lastname']  # ?ordering=-username


class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [ProfileOfUser]
