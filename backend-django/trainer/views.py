from functools import partial
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from accounts.models import User
from accounts.serializers import UserSerializer
from trainer.models import Counsel, Member_Coach, Request_Counsel
from .serializers import (
    CoachingSerializer,
    CounselSerializer,
    CounselWithoutCoachingPKSerializer,
    MemberSerializer,
    RequestCounselSerializer,
    TrainerListSerializer,
    TrainerSerializer,
)
from trainer import serializers

# 트레이너 목록 가져오기
@api_view(['GET'])
def select(request):
    trainer = User.objects.filter(grade='트레이너')
    serializer = TrainerListSerializer(trainer, many=True)
    context = {
        'Trainer_List': serializer.data,
        'Trainer_count': trainer.count()
    }
    return Response(context)

# 트레이너 상세 정보 가져오기
@api_view(['GET'])
def detail(request, pk):
    trainer = get_object_or_404(User, id=pk)
    if trainer.grade == '일반유저':
        return Response('트레이너가 아닙니다.', status=status.HTTP_400_BAD_REQUEST)

    else:    
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
def request_advice(request, coach_pk):

    # 추출한 회원 ID, 트레이너 ID로 Request_Counsel 테이블에 추가
    coaching = {
        'member': request.user.pk,
        'coach': coach_pk,
    }
    serializer = RequestCounselSerializer(data=coaching)

    if Request_Counsel.objects.filter(Q(coach_id=coach_pk) & Q(member_id=request.user.pk)).exists():
        return Response("이미 상담 신청 내역이 있습니다.", status=status.HTTP_400_BAD_REQUEST)
    else:
        if serializer.is_valid():
            serializer.save()

            trainer = User.objects.get(pk=coach_pk)
            trainer.alarm = True
            trainer.save()

        return Response(serializer.data)

# 유저 입장 - 상담 신청 승낙 후 상담 내용 조율 저장 후, 상담 내용 조회
@api_view(['GET'])
def get_request_detail(request, coach_pk):
    
    member = User.objects.get(pk=request.user.pk)
    member.alarm = False
    member.save()
    
    coaching = get_object_or_404(Member_Coach, member_id=request.user.pk, coach_id=coach_pk)
    counsel = get_object_or_404(Counsel, coaching_id=coaching.pk)
    serializer = CounselSerializer(counsel)
    return Response(serializer.data)

# 트레이너에게 온 상담 신청자 목록 조회
@api_view(['GET'])
def get_request_list(request):
    reqs = Request_Counsel.objects.filter(coach_id=request.user.pk)

    trainer = User.objects.get(pk=request.user.pk)
    trainer.alarm = False
    trainer.save()

    users = list()
    for req in reqs:
        users.append(req.member_id)
    reqmembers = User.objects.filter(pk__in=users)
    serializer = MemberSerializer(reqmembers, many=True)
    return Response(serializer.data)

# 상담 신청 수락 - 트레이너-유저 간 조율 후 상담 내용 저장
@api_view(['POST'])
def save_counsel(request, member_pk):
    member = User.objects.get(pk=member_pk)
    member.alarm = True
    member.save()

    # 트레이너-회원 관계 설정
    coaching = {
        'member': member_pk,
        'coach': request.user.pk,
    }
    coachserializer = CoachingSerializer(data=coaching)

    if Member_Coach.objects.filter(Q(coach_id=request.user.pk) & Q(member_id=member_pk)) :
        return Response('이미 예약이 되었습니다.', status=status.HTTP_400_BAD_REQUEST)

    if coachserializer.is_valid():
        coachserializer.save()

    # 트레이너-회원 관계 PK 가져오기
    coachingPK = get_object_or_404(Member_Coach, member_id=member_pk, coach_id=request.user.pk)
    print(coachingPK)
    serial = CounselWithoutCoachingPKSerializer(request.data)
    context = {
        'coaching_id': coachingPK.pk,
        'is_exercise': serial.data.get('is_exercise'),
        'is_diet': serial.data.get('is_diet'),
        'times': serial.data.get('times'),
        'start_date': serial.data.get('start_date'),
        'end_date': serial.data.get('end_date'),
        'comment': serial.data.get('comment'),
    }
    serializer = CounselSerializer(data=context)
    if serializer.is_valid():
        serializer.save()
        # 상담 신청 내역 삭제
        req = Request_Counsel.objects.filter(member_id=member_pk, coach_id=request.user.pk)
        req.delete()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 상담 신청 거절 - 상담 신청 내역 삭제
@api_view(['DELETE'])
def delete_request(request, member_pk):
    req = Request_Counsel.objects.filter(member_id=member_pk, coach_id=request.user.pk)
    if req is None:
        msg = '실패 : 신청 내역이 없습니다.'
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    req.delete()
    msg = '상담 신청을 거절하였습니다.'
    return Response(msg, status=status.HTTP_200_OK)


# 트레이너 회원 목록 가져오기
@api_view(['GET'])
def get_member_list(request, coach_pk):
    # 요청 coach_pk가 coach_id인 유저 목록 가져오기
    members = Member_Coach.objects.filter(coach_id=coach_pk)
    users = User.objects.filter(pk__in=members.values('member_id'))
    serializer = MemberSerializer(users, many=True)
    return Response(serializer.data)
  
    
# 트레이너-유저 간 상담 이력 조회
@api_view(['GET'])
def get_member_counsel_list(request, member_pk):
    coaching = get_object_or_404(Member_Coach, member_id=member_pk, coach_id=request.user.pk)
    counsel = Counsel.objects.filter(coaching_id=coaching.pk)
    serializer = CounselSerializer(counsel, many=True)
    return Response(serializer.data)


# 트레이너-유저 간 상담 내용 상세 조회
@api_view(['GET'])
def get_member_counsel(request, counsel_pk):
    counsel = get_object_or_404(Counsel, pk=counsel_pk)
    serializer = CounselSerializer(counsel)
    return Response(serializer.data)