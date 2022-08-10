from rest_framework import serializers
from GX.models import Conference, User_Conference

from trainer.models import Member_Coach
from .models import Diary, Diet, Schedule, Training_History

# 식단 정보
class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'

# 다이어리
class DiarySerializer(serializers.ModelSerializer):
    # 오늘의 식단 정보 포함
    diets = DietSerializer(many=True)
    class Meta:
        model = Diary
        fields = '__all__'

# 나의 트레이너 PK만
class MyTrainerPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member_Coach
        fields = [
            'coach_id'
        ]

class ConferencePKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ('id')

# 방 참여 테이블 정보
class ConferenceParticipateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Conference
        fields = [
            'user_id',
            'conference_id'
        ]

# 유저-트레이너 관계 PK
class MemberCoachPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member_Coach
        fields = ('id')

# 트레이닝 이력
class TrainingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Training_History
        fields = '__all__'

# 스케줄
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'