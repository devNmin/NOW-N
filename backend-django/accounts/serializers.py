
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


# 회원가입
class RegistrationSerializer(serializers.ModelSerializer):    
    password = serializers.CharField(
        max_length = 16,
        min_length = 9,
        # write_only :  password를 updating, creating 할 때는 사용되지만, serializing 할 때는 포함되지 않도록 하기 위해서
        write_only = True
    )
    token = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'grade',
            'email', 
            'name',
            'birth',
            'phone_number',
            'password',
            'nickname',
            'token',
            ]
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# 로그인
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=128, write_only=True)
    nickname = serializers.CharField(max_length=100, read_only=True)
    email = serializers.EmailField(read_only=True)
    
    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        
        if username is None:
            raise serializers.ValidationError(
                '아이디를 입력하세요.'
            )
        
        if password is None:
            raise serializers.ValidationError(
                '비밀번호를 입력하세요.'
            )
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            raise serializers.ValidationError(
                '계정이 존재하지 않습니다.'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                '이 사용자는 비활성화되었습니다.'
            )


        return {
            'username': user.username,
            'email': user.email,
            'nickname': user.nickname
        }


# 회원수정
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=16,
        min_length=9,
        write_only=True
    )
    
    class Meta:
        model = User
        fields = [
            'username',
            'grade',
            'email', 
            'name',
            'birth',
            'phone_number',
            'password',
            'nickname',
        ]
        
        read_only_fields = ('token', )
        

    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)
        

        for (key, value) in validated_data.items():

            setattr(instance, key, value)

        if password is not None:

            instance.set_password(password)


        instance.save()

        return instance