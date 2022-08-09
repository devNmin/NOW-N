from django.urls import path
from . import views

urlpatterns = [
    # 트레이너 목록 가져오기
    path('select/', views.select),

    # 트레이너 상세 정보 가져오기
    path('select/<int:pk>', views.detail),

    # 트레이너 닉네임 검색 목록 가져오기
    path('searchbynick/', views.search_by_nick),

    # 트레이너 상담 신청
    # path('counsel/<int:user_id>/<int:trainer_id>/', views.request_advice),
]
