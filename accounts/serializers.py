from rest_framework import serializers
from .models import UserProfile
# from rest_framework.serializers import ReadOnlyField

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'user', 'nickname']