from rest_framework import serializers
from .models import Conference
from accounts.models import User

# 방 목록
class ConferenceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'

# 단일 방 
class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all_'

# 유저 PK 조회
class UserPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
        ]