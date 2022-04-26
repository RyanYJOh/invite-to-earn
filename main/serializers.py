from rest_framework import serializers
from .models import Service, Invitation, Click
# from rest_framework.serializers import ReadOnlyField

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'user_kakao_id', 'service_kr', 'service_en', 'verified']

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ['id', 'user_kakao_id', 'service', 'type', 'invitation', 'desc', 'created_at']

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ['id', 'invitation', 'created_at']
