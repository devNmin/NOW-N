from django.urls import path
from . import views

urlpatterns = [
    # 식단 정보 한달 치 가져오기
    path('dietmonth/<str:current_month>', views.diet_month_list),

    # 식단 다이어리 - 오늘의 식단 정보 가져오기
    path('todaydiets/<str:today_date>', views.today_diets),

    # 식단 다이어리 - 오늘의 식단 정보 작성하기
    path('creatediets/', views.create_diets),

    # 식단 다이어리 - 식단 정보 삭제
    path('deletediets/<int:diet_pk>', views.delete_diet),

    # 식단 다이어리 - 음식 정보 PK로 조회
    path('selectfoodbypk/<int:food_pk>', views.select_food_by_pk),

    # 식단 다이어리 - 음식 정보 이름으로 검색
    path('selectfoodbyname', views.select_food_by_name),

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

    # 체중 / 목표 체중 그래프 - 일
    path('weightgraph/day', views.weight_graph_day),

    # 체중 / 목표 체중 그래프 - 주
    path('weightgraph/week', views.weight_graph_week),

    # 체중 / 목표 체중 그래프 - 월
    path('weightgraph/month', views.weight_graph_month),

    # 칼로리 그래프 - 일
    path('caloriegraph/day', views.calorie_graph_day),

    # 칼로리 그래프 - 주
    path('caloriegraph/week', views.calorie_graph_week),

    # 칼로리 그래프 - 월
    path('caloriegraph/month', views.calorie_graph_month),
]
