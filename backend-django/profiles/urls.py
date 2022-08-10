from django.urls import path
from . import views

urlpatterns = [
    # 프로필 정보 가져오기
    path('select/<int:pk>', views.select_profile),

    # 프로필 정보 수정하기 / 데일리 몸무게 저장
    path('modify/<int:user_pk>', views.modify_profile),

    # 팔로우
    path('select/<int:pk>/follow', views.follow),

    # 팔로우 목록 가져오기
    path('followlist/<int:pk>', views.follow_list),

    # 해쉬태그를 통한 검색
    # path('searchbytag/<str:tag_name>/', views.search_by_tag),
]
