from rest_framework import serializers
from GX.models import Conference, User_Conference

from trainer.models import Counsel, Member_Coach
from .models import Diet, Food, Schedule, Training_History

# 식단 정보
class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'

# 음식
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

# 나의 트레이너 PK만
class MyTrainerPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member_Coach
        fields = [
            'coach_id'
        ]

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

# 상담 이력
class CounselHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsel
        fields = [
            'id',
            'is_exercise',
            'is_diet',
            'times',
            'start_date',
            'end_date',
            'comment',
        ]