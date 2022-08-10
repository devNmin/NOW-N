from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
    HTTP_201_CREATED
)
from accounts.models import User
from accounts.serializers import UserSerializer
from trainer.models import Counsel, Member_Coach
from .models import Diary, Schedule, Training_History
from GX.models import Conference
from .serializers import (
    ConferenceParticipateSerializer,
    CounselHistorySerializer,
    DiarySerializer,
    DietSerializer,
    MemberCoachPKSerializer,
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
    print("Conference PK : ", conference.pk)
    # 유저 PK를 방 참여 테이블에 추가
    context = {
        'user_id' : pk,
        'conference_id' : conference.pk,
    }
    serializer = ConferenceParticipateSerializer(data=context)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    

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
    training = Member_Coach.objects.filter(member_id=pk)
    print("아이디 : ", training.id)
    # 유저-트레이너 관계 PK를 통해 상담 이력 찾기
    history = Counsel.objects.filter(coaching_id=training.id)
    print("이력 : ", history)
    serializer = CounselHistorySerializer(data=history, many=True)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 1:1 코칭룸 - 스케쥴 (주간 스케쥴 확인 / 스케쥴 추가)
@api_view(['GET', 'POST'])
def schedule_detail(request, pk):
    if request.method == 'GET':
        schedule = get_list_or_404(Schedule, user_id=pk)
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        context = {
            'user_id': pk,
            'day': request.data.get('day'),
            'start_time': request.data.get('start_time'),
            'end_time': request.data.get('end_time'),
        }
        serializer = ScheduleSerializer(data=context)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

# 그래프 - 일

# 그래프 - 주

# 그래프 - 월