from django.urls import path
from . import views

urlpatterns = [
    # 전체 방 조회
    path('conferences/', views.conference_list),

    # 방 생성
    path('createconference/', views.conference_create),

    # 방 상세 정보 조회 / 수정 / 삭제
    path('conferences/<int:pk>/', views.conference_detail),

    # 방 제목으로 검색
    path('searchbytitle/<str:title>/', views.search_by_title),

    # 방 방장 이름으로 검색
    path('searchbyowner/<str:owner>/', views.search_by_owner),

    # 방 정렬하여 목록 가져오기 (시간, 팔로워, 운동종류, 인원)
    path('conferencesort/<int:order>/', views.conference_sort),
]
