from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from accounts.models import User, Tag
from .serializers import (
    FollowBarSerializer,
    FollowListSerializer,
    WeightSerializer,
    ProfileSerializer,
    ProfileModifySerializer,
    TagSerializer,
)
from profiles import serializers

# 프로필 정보 가져오기
@api_view(['GET'])
def select_profile(request, pk):
    profile = get_object_or_404(User, pk=pk)
    hashtags = TagSerializer(profile.tags, many=True)
    context = {
        'name' : profile.name,
        'nickname' : profile.nickname,
        'img' : profile.img,
        'age' : profile.age,
        'gender' : profile.gender,
        'height' : profile.height,
        'weight' : profile.user_weight,
        'object_weight' : profile.object_weight,
        'followers' : profile.followers.count(),
        'followings' : profile.followings.count(),
        'hashtag' : hashtags.data
    }


    return JsonResponse(context)


# 프로필 정보 수정하기
@api_view(['PUT'])
def modify_profile(request, user_pk):
    if not User.objects.filter(pk=user_pk).exists():
        return Response('유저가 존재하지 않습니다', status=status.HTTP_400_BAD_REQUEST)
    else:
        found_user = User.objects.get(id=user_pk)
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
            return Response('본인의 프로필이 아닙니다.', status=status.HTTP_400_BAD_REQUEST)


# 팔로우 체크
@api_view(['GET'])
def checkfollow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user
    if person.pk == user.pk:
        return Response('본인입니다.')
    elif person.followers.filter(pk=user.pk).exists():
        return Response('팔로우 관계입니다.')
    else:
        return Response('팔로우 관계가 아닙니다.')
    

# 팔로우하기
@api_view(['POST'])
def follow(request, pk):
    person = get_object_or_404(get_user_model(), pk=pk)
    user = request.user
    if person.pk == user.pk:
        return Response('자기 자신입니다.')
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

        serialize = FollowListSerializer(followlist, many=True)

        context ={
            'followers': person.followers.count(),
            'followings': person.followings.count(),
            'followlist': serialize.data
        }
        return Response(context)
    else:
        return Response('본인의 팔로우 목록만 가져올 수 있습니다.')


# 팔로우 추천 인물 목록
@api_view(['GET'])
def recommend_list(request):
    list = User.objects.all()
    recommend = list.annotate(follower_count=Count('followings')).order_by('-follower_count')[:10]
    serializer = FollowBarSerializer(recommend, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


# 해시태그 추가
@api_view(['POST'])
def hashtag(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.user.pk == user.pk:
        if user.hashtag_cnt < 5:
            if not user.tags.filter(hashtag=request.data.get('hashtag')).exists():
                serializer = TagSerializer(data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    user.tags.add(serializer.data['id'])
                    user.hashtag_cnt += 1
                    user.save()
                    return Response(serializer.data , status=status.HTTP_200_OK)
            return Response('해시태그가 존재합니다.', status=status.HTTP_400_BAD_REQUEST)
        return Response('해시태그의 수가 초과되었습니다..', status=status.HTTP_400_BAD_REQUEST)
    return Response('본인의 해시태그만 추가 가능.', status=status.HTTP_400_BAD_REQUEST)


# 해시태그 삭제
@api_view(['DELETE'])
def delete_hashtag(request, user_pk, tag_pk):
    user=get_object_or_404(User, pk=user_pk)
    if request.user.pk == user.pk:
        tag=get_object_or_404(Tag, pk=tag_pk)
        user.tags.remove(tag)
        user.hashtag_cnt -= 1
        user.save()
        if tag.users.count() == 0:
            tag.delete() 
        return Response('삭제되었습니다.')
    return Response('본인의 해시태그만 삭제 가능.', status=status.HTTP_400_BAD_REQUEST)


# 해시태그 검색
@api_view(['get'])
def search_hashtag(request):
    keyword = request.data.get('hashtag')
    tag = Tag.objects.filter(hashtag = keyword)
    if tag:
        user = User.objects.filter(tags__in = tag).order_by('-pk') 
        serializer = ProfileSerializer(user, many=True)
        return Response(serializer.data)
    else:
        return Response('해당 태그가 없습니다.', status=status.HTTP_400_BAD_REQUEST)