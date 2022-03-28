from rest_framework import serializers

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('id', 'user', 'type', 'is_verified', 'sign_in_provider', 'created_at', 'updated_at')


class ProfileShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'name', 'lastname', 'type', 'is_verified', 'bio')
