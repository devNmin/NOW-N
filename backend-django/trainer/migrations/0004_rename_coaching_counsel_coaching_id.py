# Generated by Django 3.2.12 on 2022-08-08 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_alter_member_coach_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counsel',
            old_name='coaching',
            new_name='coaching_id',
        ),
    ]
