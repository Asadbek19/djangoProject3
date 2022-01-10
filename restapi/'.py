from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()


class UserSerializer2(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_active']