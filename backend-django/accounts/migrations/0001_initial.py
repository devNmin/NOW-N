# Generated by Django 3.2.12 on 2022-08-10 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(max_length=15, unique=True)),
                ('nickname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('birth', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('grade', models.CharField(choices=[('트레이너', '트레이너'), ('일반유저', '일반 유저')], default=1, max_length=10)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.IntegerField(null=True)),
                ('height', models.FloatField(null=True)),
                ('user_weight', models.FloatField(null=True)),
                ('object_weight', models.FloatField(null=True)),
                ('exercise_category', models.IntegerField(null=True)),
                ('career', models.CharField(max_length=500, null=True)),
                ('diet_price', models.IntegerField(null=True)),
                ('exercise_price', models.IntegerField(null=True)),
                ('comment', models.CharField(max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('followers', models.ManyToManyField(related_name='followings', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exercise_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pilates', models.IntegerField(default=0)),
                ('bare_body', models.IntegerField(default=0)),
                ('yoga', models.IntegerField(default=0)),
                ('stretching', models.IntegerField(default=0)),
                ('machine', models.IntegerField(default=0)),
                ('etc', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercising', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
