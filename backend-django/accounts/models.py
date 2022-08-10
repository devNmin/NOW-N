from django.db import models
from django.db.models.fields import BooleanField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

# from profiles.models import Tag

class CustomAccountManger(BaseUserManager):
    def create_superuser(self, user_id, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if user_id is None:
            raise TypeError('Superuser must have a password.')
        if password is None:
            raise TypeError('Superuser must have a password.')
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user( user_id, password, **other_fields)

    def create_user(self, user_id, password, **other_fields):

        if user_id is None:
            raise TypeError('Users must have a ID.')
        
        user = self.model(user_id=user_id,
                           **other_fields)
        user.set_password(password)
        user.save()

select_class = (
    ( '트레이너','트레이너'),
    ( '일반유저','일반 유저'),
)

class User(AbstractBaseUser, PermissionsMixin):
    # 기본 유저 필드
    user_id = models.CharField(max_length=15, unique=True)
    nickname = models.CharField(max_length=100, null=True)
    email = models.EmailField(db_index=True, unique=True)
    name = models.CharField(max_length=30)
    birth = models.IntegerField() # int
    phone_number = models.IntegerField() # int
    grade = models.CharField(max_length=10, default=1, choices=select_class) # int
    # 프로필 추가 필드
    img = models.URLField(null=True)
    age = models.IntegerField(null=True) # 나이
    gender = models.IntegerField(null=True) # 0 : 남 / 1 : 여
    height = models.FloatField(null=True) # 신장
    user_weight = models.FloatField(null=True) # 현재 체중
    object_weight = models.FloatField(null=True) # 목표 체중
    # 트레이너 추가 필드
    exercise_category = models.IntegerField(null=True) # 트레이너의 운동 종류
    career = models.CharField(max_length=500, null=True) # 경력
    diet_price = models.IntegerField(null=True) # 식단 관리 가격
    exercise_price = models.IntegerField(null=True) # 운동 가격
    comment = models.CharField(max_length=500, null=True) # 기타 추가 코맨트

    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)

    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    # tags = models.ManyToManyField(Tag, symmetrical=False, related_name='taggings')
    USERNAME_FIELD = 'user_id'

    REQUIRED_FIELDS = [
    'email',
    'name',
    'birth',
    'phone_number',
    'grade',
    ]
    
    objects = CustomAccountManger() # 일반/슈퍼 user 모두 처리

    def __str__(self):
        return self.user_id

# 회원 운동 종류 카운팅을 위한 테이블
class Exercise_Category(models.Model):
    user_id=models.ForeignKey(User, related_name='exercising', on_delete=models.CASCADE)
    pilates=models.IntegerField(default=0) # 필라테스 횟수
    bare_body=models.IntegerField(default=0) # 맨몸운동 횟수
    yoga=models.IntegerField(default=0) # 요가 횟수
    stretching=models.IntegerField(default=0) # 스트레칭 횟수
    machine=models.IntegerField(default=0) # 기구운동 횟수
    etc=models.IntegerField(default=0) # 기타 횟수