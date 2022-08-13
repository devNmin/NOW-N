from django.db import models

from accounts.models import User

# 그룹 운동 방
class Conference(models.Model):
    owner_id=models.IntegerField()
    password=models.IntegerField(null=True)
    category=models.IntegerField()
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(null=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    max_user=models.IntegerField(default=6)
    thumnail=models.TextField()
    is_active=models.BooleanField(default=True)

# 유저 - 운동 방 관계
class User_Conference(models.Model):
    conference_id=models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='entering_room')
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)