from multiprocessing import context
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from PX.serializers import ConferenceParticipateSerializer
from .models import Conference, User_Conference
from accounts.models import User
from .serializers import (
    ConferenceSerializer,
)

# 전체 방 조회
@api_view(['GET'])
def conference_list(request):
    list = Conference.objects.all()
    conferences = list.annotate(participate_count=Count('entering_room'))
    serializer = ConferenceSerializer(conferences, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

# 방 생성
@api_view(['POST'])
def conference_create(request):
    # 요청 데이터로 방 Conference 데이터 저장
    serializer = ConferenceSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # 자신도 방에 입장 -> User_Conference에 데이터 저장
        context = {
            'user_id': request.user.pk,
            'conference_id': serializer.data.get('id'),
        }
        print("User_Conference : ", context)
        conference_serializer = ConferenceParticipateSerializer(data=context)
        if conference_serializer.is_valid():
            conference_serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

# 방 입장하기
@api_view(['POST'])
def enter_room(request, pk):
    # 현재 자신이 이미 방에 참여하고 있는지 체크
    participation = User_Conference.objects.filter(conference_id=pk)
    for user in participation:
        if request.user.pk == user.user_id:
            msg = '실패 : 이미 방에 참여 중입니다.'
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    context = {
        'user_id': request.user.pk,
        'conference_id': pk,
    }
    serializer = ConferenceParticipateSerializer(data=context)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

# 방에서 퇴장하기
@api_view(['DELETE'])
def exit_room(request, pk):
    # 현재 자신이 해당하는 방에 있는 지 체크
    is_entered = User_Conference.objects.filter(user_id=request.user.pk, conference_id=pk)
    if is_entered is None:
        msg = '실패 : 해당하는 방에 참여한 정보가 없습니다.'
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    is_entered.delete()
    msg = '퇴장하였습니다.'
    return Response(msg, status=status.HTTP_200_OK)

# 방 상세 정보 조회 / 수정 / 삭제
@api_view(['GEt', 'PUT', 'DELETE'])
def conference_detail(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    # 조회
    if request.method == 'GET':
        serializer = ConferenceSerializer(conference)
        participate = User_Conference.objects.filter(conference_id=pk)
        context = {
            'owner_id': serializer.data.get('owner_id'),
            'password': serializer.data.get('password'),
            'category': serializer.data.get('category'),
            'start_time': serializer.data.get('start_time'),
            'end_time': serializer.data.get('end_time'),
            'title': serializer.data.get('title'),
            'description': serializer.data.get('description'),
            'max_user': serializer.data.get('max_user'),
            'thumnail': serializer.data.get('thumnail'),
            'is_active': serializer.data.get('is_active'),
            'participate_count': participate.count(),
        }
        return JsonResponse(context)
    # 수정
    elif request.method == 'PUT':
        serializer = ConferenceSerializer(conference, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    # 삭제
    elif request.method == 'DELETE':
        conference.delete()
        msg = '삭제되었습니다.'
        return Response(msg, status=HTTP_204_NO_CONTENT)
        
# 방 제목으로 검색
@api_view(['GET'])
def search_by_title(request, title):
    conference = Conference.objects.filter(title__icontains=title)
    serializer = ConferenceSerializer(conference, many=True)

    return Response(serializer.data)

# 방 방장 이름으로 검색
@api_view(['GET'])
def search_by_owner(request, owner):
    user_pk = User.objects.filter(user_id__icontains=owner)
    conference = Conference.objects.filter(owner_id__in=user_pk)
    serializer = ConferenceSerializer(conference, many=True)

    return Response(serializer.data)

# 방 정렬하여 목록 가져오기 (시간, 팔로워, 인원)
@api_view(['GET'])
def conference_sort(request, order):
    # 시간순
    if order == 0:
        conference = Conference.objects.order_by('-start_time')
        serializer = ConferenceSerializer(conference, many=True)
        return Response(serializer.data)
    # 방장 팔로워순
    # 인원순