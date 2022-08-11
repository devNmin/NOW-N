from functools import partial
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User
from trainer.models import Member_Coach
from .serializers import (
    CoachingPKSerializer,
    CoachingSerializer,
    CounselSerializer,
    TrainerListSerializer,
    TrainerSerializer,
)

# 트레이너 목록 가져오기
@api_view(['GET'])
def select(request):
    trainer = User.objects.filter(grade='트레이너')
    serializer = TrainerListSerializer(trainer, many=True)
    return Response(serializer.data)

# 트레이너 상세 정보 가져오기
@api_view(['GET'])
def detail(request, pk):
    trainer = get_object_or_404(User, id=pk)

    coaching = Member_Coach.objects.filter(coach=pk)
    if coaching is None:
        member_count = 0
    else:
        member_count = coaching.count()

    context = {
        'name' : trainer.name,
        'nickname' : trainer.nickname,
        'exercise_category' : trainer.exercise_category,
        'followers' : trainer.followers.count(),
        'age' : trainer.age,
        'gender' : trainer.gender,
        'career' : trainer.career,
        'members' : member_count,
        'diet_price' : trainer.diet_price,
        'exercise_price' : trainer.exercise_price,
        'comment' : trainer.comment,
    }

    return JsonResponse(context)

# 트레이너 상세 정보 수정
@api_view(['PUT'])
def modify(request, pk):
    # 트레이너 PK로 정보 조회
    trainer = get_object_or_404(User, pk=pk)

    if request.user.pk == trainer.pk:
        serializer = TrainerSerializer(trainer, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        msg = '실패 : 본인만 수정가능합니다.'
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

# 트레이너 닉네임 검색 목록 가져오기
@api_view(['GET'])
def search_by_nick(request, nickname):
    trainer = User.objects.filter(grade__exact='트레이너', nickname__icontains=nickname)
    serializer = TrainerListSerializer(trainer, many=True)
    return Response(serializer.data)

# 상담 신청 하기
@api_view(['POST'])
def request_advice(request, user_pk, coach_pk):
    # 추출한 회원 ID, 트레이너 ID로 Member_Coach 테이블에 추가
    coaching = {
        'member': user_pk,
        'coach': coach_pk,
    }
    serializer = CoachingSerializer(data=coaching)
    if Member_Coach.objects.filter(coach_id=coach_pk).exists() and Member_Coach.objects.filter(member_id=user_pk).exists():
        return Response("이미 상담예약이 있습니다.", status=status.HTTP_400_BAD_REQUEST)
    else:
        if serializer.is_valid():
            serializer.save()
    
    # 추가된 Member_Coach 테이블 하위의 Counsel 테이블에 상담 기록 추가
    coaching_id = get_object_or_404(Member_Coach, member_id=user_pk)
    serial = CounselSerializer(data=request.data)
    serial.is_valid()
    print("코칭 필드 : ???", coaching_id.pk)
    context = {
        'is_exercise': serial.data.get('is_exercise'),
        'is_diet': serial.data.get('is_diet'),
        'times': serial.data.get('times'),
        'start_date': serial.data.get('start_date'),
        'end_date': serial.data.get('end_data'),
        'comment': serial.data.get('comment'),
        'coaching_id': coaching_id.pk,
    }
    print("코칭 필드 : ???휴휴", context)
    coachserailizer = CounselSerializer(data=context)
    print(coachserailizer)
    if coachserailizer.is_valid(raise_exception=True):
        coachserailizer = coachserailizer.save()
    sentece='상담신청완료'
    return Response(sentece,status=status.HTTP_200_OK)