from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from django.shortcuts import get_object_or_404
from .models import Conference
from accounts.models import User
from .serializers import (
    ConferenceListSerializer,
    ConferenceSerializer,
)

# 전체 방 조회
@api_view(['GET'])
def conference_list(request):
    conference = Conference.objects.order_by('-pk')
    serializer = ConferenceListSerializer(conference, many=True)
    return Response(serializer.data)

# 방 생성
@api_view(['POST'])
def conference_create(request):
    serializer = ConferenceSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

# 방 상세 정보 조회 / 수정 / 삭제
@api_view(['GEt', 'PUT', 'DELETE'])
def conference_detail(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    # 조회
    if request.method == 'GET':
        serializer = ConferenceSerializer(conference)
        return Response(serializer.data)
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
    serializer = ConferenceListSerializer(conference, many=True)

    return Response(serializer.data)

# 방 방장 이름으로 검색
@api_view(['GET'])
def search_by_owner(request, owner):
    user_pk = User.objects.filter(user_id__icontains=owner)
    conference = Conference.objects.filter(owner_id__in=user_pk)
    serializer = ConferenceListSerializer(conference, many=True)

    return Response(serializer.data)

# 방 정렬하여 목록 가져오기 (시간, 팔로워, 인원)
@api_view(['GET'])
def conference_sort(request, order):
    # 시간순
    if order == 0:
        conference = Conference.objects.order_by('-start_time')
        serializer = ConferenceListSerializer(conference, many=True)
        return Response(serializer.data)
    # 방장 팔로워순
    # 인원순