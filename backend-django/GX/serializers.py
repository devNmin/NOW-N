from rest_framework import serializers
from .models import Conference, User_Conference
from accounts.models import User

# 방 목록
class ConferenceListSerializer(serializers.ModelSerializer):
    participate_count = serializers.IntegerField()
    class Meta:
        model = Conference
        fields = '__all__'

# 단일 방 
class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'

# 유저 PK 조회
class UserPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
        ]

# 방에 참여한 유저
class ParticipateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Conference
        fields = [
            'user_id',
        ]