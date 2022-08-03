from rest_framework import serializers
from accounts.models import User

class TrainerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'name',
            'nickname',
        ]
