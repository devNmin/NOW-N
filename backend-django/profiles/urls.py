from django.urls import path
from . import views

urlpatterns = [
    # 프로필 정보 가져오기
    path('select/<int:pk>', views.select_profile),

    # 프로필 정보 수정하기 / 데일리 몸무게 저장
    path('modify/<int:user_pk>', views.modify_profile),

    # 팔로우 했는지 확인
    path('checkfollow/<int:user_pk>', views.checkfollow),

    # 팔로우
    path('select/<int:pk>/follow', views.follow),

    # 팔로우 목록 가져오기
    path('followlist/<int:pk>', views.follow_list),

    # 팔로우 추천 인물 목록 가져오기
    path('recommendlist', views.recommend_list),

    # 해쉬태그 추가
    path('hashtag/<int:user_pk>/', views.hashtag),

    # 해쉬태그 삭제
    path('hashtag/<int:user_pk>/<tag_pk>/', views.delete_hashtag),

    # 해쉬태그 검색
    path('search_hashtag/', views.search_hashtag),
]
