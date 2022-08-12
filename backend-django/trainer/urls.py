from django.urls import path
from . import views

urlpatterns = [
    # ------- 유저 입장 ---------
    # 트레이너 목록 가져오기
    path('select/', views.select),

    # 트레이너 상세 정보 가져오기
    path('select/<int:pk>', views.detail),

    # 트레이너 상세 정보 수정
    path('modify/<int:pk>', views.modify),

    # 트레이너 닉네임 검색 목록 가져오기
    path('searchbynick/<str:nickname>', views.search_by_nick),

    # 트레이너 상담 신청
    path('counsel/<int:coach_pk>', views.request_advice),

    # 유저 입장 - 상담 신청 승낙 후 상담 내용 조율 저장 후, 상담 내용 조회
    path('getrequestdetail/<int:coach_pk>', views.get_request_detail),




    #------- 트레이너 입장--------
    # 트레이너에게 온 상담 신청자 목록 조회
    path('getrequestlist/', views.get_request_list),

    # 상담 신청 수락 - 트레이너-유저 간 조율 후 상담 내용 저장
    path('savecounsel/<int:member_pk>', views.save_counsel),

    # 상담 신청 거절 - 상담 신청 내역 삭제
    path('deleterequest/<int:member_pk>', views.delete_request),

    # 트레이너 회원 목록 가져오기
    path('getmemberlist/<int:coach_pk>', views.get_member_list),

    # 트레이너-유저 간 상담 이력 조회
    path('getmembercounsellist/<int:member_pk>', views.get_member_counsel_list),

    # 트레이너-유저 간 상담 내용 상세 조회
    path('getmembercounsel/<int:counsel_pk>', views.get_member_counsel),
]
