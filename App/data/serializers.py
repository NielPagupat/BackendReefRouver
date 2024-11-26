from rest_framework import serializers
from .models import DataEntry
from App.users.models import CustomUser

class DataEntrySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),  # Allow selection from all users
        required=True)

    class Meta:
        model = DataEntry
        fields = ['id', 'owner', 'location', 'csv', 'videos', 'uploaded_at']
        read_only_fields = ['owner', 'uploaded_at']
    
    def get_csv(self, obj):
        # Generate the full URL for the CSV file
        request = self.context.get('request')
        if obj.csv and request:
            return request.build_absolute_uri(obj.csv.url)
        return None

    def get_videos(self, obj):
        # Generate the full URL for the video file
        request = self.context.get('request')
        if obj.videos and request:
            return request.build_absolute_uri(obj.videos.url)
        return None