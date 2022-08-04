# Generated by Django 3.2.12 on 2022-08-03 08:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GX', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='Participates',
            field=models.ManyToManyField(related_name='Participating', to=settings.AUTH_USER_MODEL),
        ),
    ]