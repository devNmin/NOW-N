from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED
)
from accounts.models import User
from accounts.serializers import UserSerializer
from trainer.models import Counsel, Member_Coach
from trainer.serializers import CounselSerializer
from .models import Diary, Schedule, Training_History
from GX.models import Conference
from .serializers import (
    ConferencePKSerializer,
    ConferenceParticipateSerializer,
    DiarySerializer,
    DietSerializer,
    MemberCoachPKSerializer,
    MyTrainerPKSerializer,
    ScheduleSerializer,
    TrainingHistorySerializer,
)

# 회원 다이어리 가져오기
@api_view(['GET'])
def diary_list(request, userID):
    diaries = get_list_or_404(Diary, userID=userID)
    serializer = DiarySerializer(diaries, many=True)
    return Response(serializer.data)

# 식단 다이어리 - 오늘의 식단 정보 가져오기
@api_view(['GET'])
def today_diets(request, diaryID):
    diets = get_list_or_404(Diary, diaryID=diaryID)
    serializer = DietSerializer(diets, many=True)
    return Response(serializer.data)

# 식단 다이어리 - 오늘의 식단 정보 작성하기 (음식 카테고리 선택)

# 식단 다이어리 - 오늘의 식단 정보 작성하기 (음식 검색하기)

# 1:1 코칭룸 - 나의 트레이너 정보 가져오기
@api_view(['GET'])
def mytrainer(request, pk):
    # 자신의 PK로 트레이너 관계인 트레이너 PK 추출
    training = get_object_or_404(Member_Coach, member_id=pk)
    print("내 트레이너 : ", training.coach_id)
    # 트레이너 PK를 이용해 트레이너 정보 가져오기
    trainer = get_object_or_404(User, pk=training.coach_id)
    serializer = UserSerializer(trainer)
    return Response(serializer.data)

# 1:1 코칭룸 - 나의 트레이너 1:1 코칭룸 입장
@api_view(['POST'])
def enter_room(request, pk):
    # 자신의 PK로 트레이너 관계인 트레이너 PK 추출
    training = get_object_or_404(Member_Coach, member_id=pk)
    # 트레이너 pk가 owner_id인 방 정보 추출
    conference = get_object_or_404(Conference, owner_id=training.coach_id)
    conferencePK = ConferencePKSerializer(conference)
    # 유저 PK를 방 참여 테이블에 추가
    context = {
        'user_id' : pk,
        'confernece_id' : conferencePK,
    }
    serializer = ConferenceParticipateSerializer(context)
    serializer.save()
    

# 1:1 코칭룸 - 커뮤니티 (이전 코칭 기록 가져오기)
@api_view(['GET'])
def train_history(request, pk):
    # 회원 PK를 통해 유저-트레이너 관계 PK 찾기
    training = Member_Coach.objects.get(member_id=pk)
    trainingPK = MemberCoachPKSerializer(training)
    # 유저-트레이너 관계 PK를 통해 트레이닝 이력 가져오기
    history = Training_History.objects.get(pk=trainingPK)
    serializer = TrainingHistorySerializer(history)

    return Response(serializer.data)

# 1:1 코칭룸 - 상담이력 (상담이력 가져오기)
@api_view(['GET'])
def counsel_history(request, pk):
    # 회원 PK를 통해 유저-트레이너 관계 PK 찾기
    training = Member_Coach.objects.get(member_id=pk)
    trainingPK = MemberCoachPKSerializer(training)
    # 유저-트레이너 관계 PK를 통해 상담 이력 찾기
    history = Counsel.objects.get(coachingID=trainingPK)
    serializer = CounselSerializer(history)

    return Response(serializer.data)

# 1:1 코칭룸 - 스케쥴 (주간 스케쥴 확인 / 스케쥴 추가)
@api_view(['GET', 'POST'])
def schedule_detail(request, pk):
    schedule = get_list_or_404(Schedule, user_id=pk)
    if request.method == 'GET':
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ScheduleSerializer(request.data)
        serializer.save()
        return Response(status=HTTP_201_CREATED)

# 그래프 - 일

# 그래프 - 주

# 그래프 - 월