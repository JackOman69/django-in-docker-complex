from rest_framework.serializers import Serializer
from rest_framework import serializers

class GetAttachmentSerializer(Serializer):
    
    server_name = serializers.CharField()
    club_id = serializers.IntegerField()