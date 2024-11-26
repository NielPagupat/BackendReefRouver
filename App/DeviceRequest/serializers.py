from rest_framework import serializers
from .models import device, AccessRequestHistory, DeviceRequestAccess
from django.contrib.auth import get_user_model

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = ['id', 'device_name', 'device_status']

User = get_user_model()

class DeviceRequestAccessSerializer(serializers.ModelSerializer):
    # Use the primary key for input but include nested details for output
    device = serializers.PrimaryKeyRelatedField(queryset=device.objects.all())  # Accept device ID as input
    device_details = DeviceSerializer(source='device', read_only=True)  # Return nested details of device

    requestee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Use primary key to get the user

    class Meta:
        model = DeviceRequestAccess
        fields = [
            'id',
            'requestee',
            'device',  # Accept device ID here
            'device_details',  # Include nested device details in output
            'dateRequested',
            'dateTobeUsed',
            'accessDuration',
            'requestStatus',
        ]

class AccessRequestHistorySerializer(serializers.ModelSerializer):
    accessid = DeviceRequestAccessSerializer()  # Nested serializer to include details of the access request

    class Meta:
        model = AccessRequestHistory
        fields = ['id', 'accessid', 'dateapproved']