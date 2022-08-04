from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Weight
from accounts.models import User
from .serializers import (
    ProfileSerializer,
    WeightSerializer,
)
from profiles import serializers

# 프로필 정보 가져오기
@api_view(['GET'])
def select_profile(request, pk):
    profile = get_object_or_404(User, pk=pk)
    context = {
        'name' : profile.name,
        'age' : profile.age,
        'gender' : profile.gender,
        'height' : profile.height,
        'weogjt' : profile.weight,
        'object_weight' : profile.object_weight,
        'followers' : profile.followers.count(),
    }

    return JsonResponse(context)

# 프로필 정보 수정하기
@api_view(['PUT'])
def modify_profile(request, pk):
    # 프로필 데이터 수정 저장
    profile = get_object_or_404(User, pk=pk)
    serializer = ProfileSerializer(profile, request.data)
    serializer.save()

    # 프로필 데이터 중 몸무게 데이터 따로 저장
    context = {
        'user_id' : profile.pk,
        'weight' : request.get('weight')
    }
    weight_serializer = WeightSerializer(context)
    weight_serializer.save()

    return Response(serializer.data)

# 팔로우하기
@api_view(['POST'])
def follow(request, pk):
    person = get_object_or_404(User, pk=pk)
    if person.pk != request.data.pk:
        if person.followers.filter(pk=request.data.pk).exists():
            person.followers.remove(request.data)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profiles', person.pk)

# 해시태그를 통한 유저 검색
# @api_view(['GET'])
# def search_by_tag(request, tag_name):
#     tag = get_object_or_404(Tag, tag_name=tag_name)
#     serializer = TagPKSerializer(tag)