from unicodedata import category
from django.db import models
from accounts.models import User
from trainer.models import Member_Coach

# 식단
class Diet(models.Model):
    userID=models.ForeignKey(User, on_delete=models.CASCADE)# 유저 PK
    picture=models.TextField(null=True, blank=True)
    category=models.CharField(max_length=20) # 분류필드 : 아침, 점심, 저녁 ...
    date=models.CharField(max_length=20) # 날짜 : 20220816
    time=models.CharField(max_length=100) # 시간 : 1250AM
    comment=models.TextField(null=True, blank=True)
    total_calorie=models.FloatField(null=True, blank=True)
    new_date=models.DateField(null=True, blank=True)

# 음식
class Food(models.Model):
    category=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    serving_size=models.IntegerField(null=True)
    unit=models.CharField(max_length=10)
    kcal=models.FloatField(null=True)
    water=models.FloatField(null=True)
    protein=models.FloatField(null=True)
    fat=models.FloatField(null=True)
    carbohydrate=models.FloatField(null=True)
    sugar=models.FloatField(null=True)
    glucose=models.FloatField(null=True)
    calcium=models.FloatField(null=True)
    natrium=models.FloatField(null=True)

# 식단_음식 관계
class Diet_Food(models.Model):
    diet=models.ForeignKey(Diet, on_delete=models.CASCADE)
    food=models.ForeignKey(Food, on_delete=models.CASCADE)
    size=models.IntegerField(null=True)
    name=models.CharField(max_length=100)

# 트레이닝 이력
class Training_History(models.Model):
    coachingID=models.ForeignKey(Member_Coach, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    comment=models.CharField(max_length=500)

# 스케줄
class Schedule(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    day=models.IntegerField(null=True) # 0~6 : 월 ~ 일
    start_time=models.IntegerField(null=True)
    end_time=models.IntegerField(null=True)