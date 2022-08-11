from django.urls import path
from . import views

urlpatterns = [
    # 회원 다이어리 가져오기
    path('diaries/<int:userID>', views.diary_list),

    # 식단 다이어리 - 오늘의 식단 정보 가져오기
    path('todaydiets/<int:diaryID>', views.today_diets),

    # 식단 다이어리 - 오늘의 식단 정보 작성하기

    # 1:1 코칭룸 - 나의 트레이너 정보 가져오기
    path('mytrainer/<int:pk>', views.mytrainer),

    # 1:1 코칭룸 - 코칭룸 정보 조회 / 수정
    path('coachingroom/<int:pk>', views.coachingroom),

    # 1:1 코칭룸 - 코칭룸 On/Off
    path('coachingroomonoff/<int:pk>', views.coachingroomonoff),

    # 1:1 코칭룸 - 나의 트레이너 1:1 코칭룸 입장
    path('enterroom/<int:pk>', views.enter_room),

    # 1:1 코칭룸 - 커뮤니티 (이전 코칭 기록 가져오기)
    path('trainhistory/<int:pk>', views.train_history),

    # 1:1 코칭룸 - 상담이력 (상담이력 가져오기)
    path('counselhistory/<int:pk>', views.counsel_history),

    # 1:1 코칭룸 - 스케쥴 (주간 스케쥴 확인 / 스케쥴 추가)
    path('schedule/<int:pk>', views.schedule_detail),

    # 그래프 - 일

    # 그래프 - 주

    # 그래프 - 월
]
