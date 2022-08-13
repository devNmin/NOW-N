from rest_framework import serializers
from accounts.models import User
from trainer.models import Counsel, Member_Coach, Request_Counsel

class RequestCounselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request_Counsel
        fields = '__all__'

class CoachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member_Coach
        fields = '__all__'

class TrainerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'nickname',
            'exercise_category',
            'diet_price',
            'exercise_price',
            'is_active',
        ]

class CounselWithoutCoachingPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsel
        fields = [
            'is_exercise',
            'is_diet',
            'times',
            'start_date',
            'end_date',
            'comment',
        ]

class CounselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsel
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# 회원 정보
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'nickname',
            'age',
            'gender',
            'height',
            'user_weight',
            'object_weight',
        ]
