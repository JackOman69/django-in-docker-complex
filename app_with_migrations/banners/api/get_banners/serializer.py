from rest_framework.serializers import Serializer
from rest_framework import serializers

class GetBannersSerializer(Serializer):
    
    server_name = serializers.CharField(allow_blank=True, required=False)
    club_id = serializers.IntegerField(allow_null=True, default=None, required=False)