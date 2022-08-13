from django.db import models
from accounts.models import User
from trainer.models import Member_Coach

# 다이어리
class Diary(models.Model):
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField() # 다이어리 해당일
    calories=models.IntegerField() # 해당일 칼로리

# 식단
class Diet(models.Model):
    diaryID=models.ForeignKey(Diary, on_delete=models.CASCADE)# 식단 정보가 입력될 다이어리 PK
    moment=models.IntegerField()# 식단 입력 시간 (아침, 점심, 저녁, 간식)
    time=models.DateTimeField()# 식단 입력 시각
    picture=models.TextField()
    comment=models.CharField(max_length=500)

# 트레이닝 이력
class Training_History(models.Model):
    coachingID=models.ForeignKey(Member_Coach, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    comment=models.CharField(max_length=500)

# 스케줄
class Schedule(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    day=models.IntegerField() # 0~6 : 월 ~ 일
    start_time=models.IntegerField()
    end_time=models.IntegerField()