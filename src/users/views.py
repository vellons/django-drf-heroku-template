from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from users.models import Profile
from users.serializers import ProfileSerializer


class ProfileCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all().order_by('created_at')
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['username', 'name', 'surname', 'type', 'is_active', 'is_verified']
    search_fields = ['username', 'name', 'surname']  # ?search=LIKE in all these fields
    ordering_fields = ['username', 'name', 'surname', 'created_at', 'updated_at']  # ?ordering=-created_at


class ProfileRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
