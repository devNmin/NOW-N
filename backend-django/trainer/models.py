from django.db import models
from accounts.models import User
    
class Member_Coach(models.Model):
    member = models.ForeignKey(User, related_name='create_members', on_delete=models.CASCADE)
    coach = models.ForeignKey(User, related_name='create_coaches' ,on_delete=models.CASCADE)

# 트레이너 상담 테이블
class Counsel(models.Model):
    coaching_id = models.ForeignKey(Member_Coach, on_delete=models.CASCADE)
    is_exercise = models.BooleanField()
    is_diet = models.BooleanField()
    times = models.IntegerField()
    start_date = models.DateField
    end_date = models.DateField
    comment = models.CharField(max_length=500)