from rest_framework import serializers
from .models import Service, Invitation, Click
# from rest_framework.serializers import ReadOnlyField

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'service_kr', 'service_en', 'logo_img', 'verified']

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'service', 'user', 'type', 'invitation', 'desc', 'totalClicks', 'created_at']

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'invitation', 'created_at']
