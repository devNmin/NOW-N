from rest_framework import serializers
from .models import Weight
from accounts.models import User

# 유저 pk
class UserPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id')

# 팔로우 Bar에 들어갈 정보
class FollowBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'nickname',
            'is_active',
        ]

# 팔로우 목록
class FollowListSerializer(serializers.ModelSerializer):
    followings = FollowBarSerializer(many=True, read_only=True)

# 태그 이름
# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fileds = '__all__'

# 태그 pk
# class TagPKSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ('id')

# 프로필 정보
class ProfileSerializer(serializers.ModelSerializer):
    followings = UserPKSerializer(many=True, read_only=True)
    # taggings = TagSerializer(many=True)
    class Meta:
        model = User
        fields = [
            'name',
            'age',
            'gender',
            'height',
            'user_weight',
            'object_weight',
            'followings',
        ]

class ProfileModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'nickname',
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
            'user',
            'weight',
        ]