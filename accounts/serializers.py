from rest_framework import serializers
from .models import UserProfile, User
from rest_framework import viewsets
# from rest_framework.serializers import ReadOnlyField

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields = ['id', 'user', 'nickname']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer