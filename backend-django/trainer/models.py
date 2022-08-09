from django.db import models
from accounts.models import User

# 트레이너와 일반 회원의 관계 테이블
class coaching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.CharField(max_length=100)
    

class Counsel(models.Model):
    coachID = models.ForeignKey(User, on_delete=models.CASCADE)
    is_exercise = models.BooleanField()
    is_diet = models.BooleanField()
    times = models.IntegerField()
    start_date = models.DateField
    end_date = models.DateField
    comment = models.CharField(max_length=500)