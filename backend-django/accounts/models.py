from django.db import models
from django.db.models.fields import BooleanField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

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
    user_id = models.CharField(max_length=15, unique=True)
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    name = models.CharField(max_length=30)
    birth = models.IntegerField() # int
    phone_number = models.IntegerField() # int
    grade = models.CharField(max_length=10, default=1, choices=select_class) # int

    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)


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