from django.db import models

from accounts.models import User

class Conference(models.Model):
    owner_id=models.IntegerField()
    password=models.IntegerField(null=True)
    category=models.IntegerField()
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(null=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    max_user=models.IntegerField(default=6)
    thumnail=models.URLField()
    is_active=models.BooleanField(default=True)

    Participates = models.ManyToManyField(User, symmetrical=False, related_name='Participating')