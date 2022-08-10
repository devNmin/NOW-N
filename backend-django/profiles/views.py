from functools import partial
from django.db.models import Count
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer
from .models import Weight
from accounts.models import User
from .serializers import (
    FollowBarSerializer,
    FollowListSerializer,
    WeightSerializer,
    ProfileModifySerializer
)
from profiles import serializers

# 프로필 정보 가져오기
@api_view(['GET'])
def select_profile(request, pk):
    profile = get_object_or_404(User, pk=pk)
    context = {
        'name' : profile.name,
        'img' : profile.img,
        'age' : profile.age,
        'gender' : profile.gender,
        'height' : profile.height,
        'weight' : profile.user_weight,
        'object_weight' : profile.object_weight,
        'followers' : profile.followers.count(),
    }

    return JsonResponse(context)

# 프로필 정보 수정하기
@api_view(['PUT'])
def modify_profile(request, user_pk):
    found_user = User.objects.get(id=user_pk)

    if found_user is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        if request.user.pk == found_user.pk:
            serializer = ProfileModifySerializer(found_user, data=request.data, partial=True)
            if serializer.is_valid():
                # 프로필 데이터 중 몸무게 데이터 따로 저장
                context = {
                'user' : user_pk,
                'weight' : serializer.validated_data.get('user_weight'),
                }
                weight_serializer = WeightSerializer(data=context)
                if weight_serializer.is_valid():
                    weight_serializer.save()
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    ''' 
        serializer = UserPointUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            person = get_object_or_404(get_user_model(),username=username)
            user_point = serializer.validated_data.get('point')
            person.point = user_point
            person.save()
            
            return Response(person.point)
    '''

# 팔로우하기
@api_view(['POST'])
def follow(request, pk):
    person = get_object_or_404(get_user_model(), pk=pk)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            follow = False
        else:
            person.followers.add(user)
            follow = True

    follow_status ={
        'follow':follow,
        'my_count':user.followings.count(),
    }
    return JsonResponse(follow_status)

# 팔로우 목록 가져오기
@api_view(['GET'])
def follow_list(request, pk):
    person = get_object_or_404(get_user_model(), pk=pk)
    if request.user.pk == person.pk:

        followlist = person.followings.all()
        serialized = FollowListSerializer(followlist, many=True)

        context ={
            'followers': person.followers.count(),
            'followings': person.followings.count(),
            'followlist': serialized.data
        }
        return Response(context)
            
# 팔로우 추천 인물 목록
@api_view(['GET'])
def recommend_list(request):
    list = User.objects.all()
    recommend = list.annotate(follower_count=Count('followings')).order_by('-follower_count')[:10]
    serializer = FollowBarSerializer(recommend, many=True)
    print("Recommend List : ", serializer.data)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

# 해시태그를 통한 유저 검색
# @api_view(['GET'])
# def search_by_tag(request, tag_name):
#     tag = get_object_or_404(Tag, tag_name=tag_name)
#     serializer = TagPKSerializer(tag)