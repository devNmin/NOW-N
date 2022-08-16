from django.db import models
from accounts.models import User

class Weight(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    weight=models.FloatField()
    date=models.DateField(auto_now_add=True)
