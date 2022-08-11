# Generated by Django 3.2.12 on 2022-08-10 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainer', '0001_initial'),
        ('PX', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='training_history',
            name='coachingID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.member_coach'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='diet',
            name='diaryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PX.diary'),
        ),
        migrations.AddField(
            model_name='diary',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
