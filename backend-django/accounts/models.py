import jwt
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.db.models.fields import BooleanField
from datetime import datetime, timedelta


# 유저를 생성할 때 사용하는 헬퍼(Helper) 클래스
class UserManager(BaseUserManager):
    # 관리자를 포함한 모든 사용자를 생성할 때 실행되는 함수
    def create_user(self, username, email, password=None, **extra_fields):
    
        if username is None:
            raise TypeError('Users must have a ID.')

        if email is None:
            raise TypeError('Users must have an email address.')

        if password is None:
            raise TypeError('Users must have a password.')
    
        user = self.model(
        username = username,
        # 중복 최소화를 위한 정규화
        email=self.normalize_email(email),
        **extra_fields
        )

        # django 에서 제공하는 password 설정 함수
        user.set_password(password)
        user.save()
        
        return user

    # 관리자를 생성할 때 실행되는 함수
    def create_superuser(self, username, email, password, **extra_fields):
    
        if password is None:
            raise TypeError('Superuser must have a password.')
        
        # "create_user"함수를 이용해 우선 사용자를 DB에 저장
        user = self.create_user(username, email, password, **extra_fields)
        # 관리자로 지정
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user

select_class = (
    ( 1,'트레이너'),
    ( 2,'일반 유저'),
)

# 실제 모델(Model)에 AbstractBaseUser을 상속해서 생성해주는 클래스
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True)
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    name = models.CharField(max_length=30)
    birth = models.IntegerField() # int
    phone_number = models.IntegerField() # int
    grade = models.CharField(max_length=10, default=1, choices=select_class) # int

    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    
    # 로그인 ID
    USERNAME_FIELD = 'username'
    
    # 필수로 값을 받아야 하는 필드
    REQUIRED_FIELDS = [
        'nickname',
        'email',
        'name',
        'birth',
        'phone_number',
        'grade',
    ]
    
    objects = UserManager()
    
    @property
    def token(self):
        return self._generate_jwt_token( )

    def _generate_jwt_token(self):
        dt = datetime.now( ) + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
    
        return token
    def __str__(self):
        return self.nickname