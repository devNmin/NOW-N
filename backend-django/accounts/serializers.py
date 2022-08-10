from accounts.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


# 회원가입
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 16,
        min_length = 8,
        # write_only :  password를 updating, creating 할 때는 사용되지만, serializing 할 때는 포함되지 않도록 하기 위해서
        write_only = True
    ),

    class Meta:
        model = User
        fields = [
            'user_id',
            'grade',
            'email', 
            'name',
            'birth',
            'phone_number',
            'password',
            'id',
            ]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    # 중복 체크
    def validate(self, attrs):
        user_id = attrs['user_id']
        password = attrs['password']
        email = attrs['email']

        if User.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError("user_id already exists")

        elif User.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already exists") 

        return attrs


# 로그인
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# 회원정보 조회 / 수정
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=16,
        min_length=9,
        write_only=True
    )

    
    class Meta:
        model = User
        fields = [
            'id',
            'user_id',
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


# 비밀번호 번경
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('old_password', 'new_password')
        extra_kwargs = {'new_password': {'write_only': True, 'required': True},
                        'old_password': {'write_only': True, 'required': True}}

    def validate_new_password(self, value):
        validate_password(value)
        return value


# 토큰 재발급
class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token is invalid or expired'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


