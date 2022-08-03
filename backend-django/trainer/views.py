from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User
from trainer.models import coaching
from .serializers import (
    TrainerListSerializer,
)
from trainer import serializers

# 트레이너 목록 가져오기
@api_view(['GET'])
def select(request):
    trainer = User.objects.get(grade='트레이너')
    serializer = TrainerListSerializer(trainer, many=True)
    return Response(serializer.data)

# 트레이너 상세 정보 가져오기
@api_view(['GET'])
def detail(request, pk):
    trainer = get_object_or_404(User, pk=pk)
    coaching = get_list_or_404(coaching, trainer_id=pk)

    context = {
        'name' : trainer.name,
        'nickname' : trainer.nickname,
        'age' : trainer.age,
        'gender' : trainer.gender,
        'members' : coaching.count()
    }

    return JsonResponse(context)

# 트레이너 닉네임 검색 목록 가져오기
@api_view(['GET'])
def search_by_nick(request, nickname):
    trainer = User.objects.filter(grade__exact='트레이너', nickname__icontains=nickname)
    serializer = TrainerListSerializer(trainer, many=True)
    return Response(serializer.data)

# 상담 신청 하기
@api_view(['POST'])
def search_by_nick(request, user_id, trainer_id):
    # 상담 신청만으로 일반회원-트레이너의 관계가 성립하는가
    # 스케줄 조정이 신청서만으로 가능한가
    pass