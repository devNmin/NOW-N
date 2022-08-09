from rest_framework import serializers
from accounts.models import User
from trainer.models import Counsel, Member_Coach

class CoachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member_Coach
        fields = '__all__'

class CoachingPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member_Coach
        fields = [
            'id',
        ]

class TrainerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'nickname',
            'is_active',
        ]

class CounselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsel
        fields = [
            'coaching_id',
            'is_exercise',
            'is_diet',
            'times',
            'start_date',
            'end_date',
            'comment',
        ]

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
