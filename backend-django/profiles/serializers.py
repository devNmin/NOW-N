from rest_framework import serializers
from .models import Weight
from accounts.models import User, Tag

# 유저 pk
class UserPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id')

# 유저 모든 정보
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# 팔로우 Bar에 들어갈 정보
class FollowBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'nickname',
            'img',
            'is_active',
        ]

# 팔로우 목록
class FollowListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    nickname = serializers.CharField(max_length=100)


# 태그 이름
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



# 프로필 정보
class ProfileSerializer(serializers.ModelSerializer):
    followings = UserPKSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'img',
            'age',
            'gender',
            'height',
            'user_weight',
            'object_weight',
            'followings',
        ]


# 프로필 수정
class ProfileModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'nickname',
            'img',
            'age',
            'gender',
            'height',
            'user_weight',
            'object_weight',
        ]

# 몸무게
class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = [
            'id',
            'user',
            'weight',
        ]