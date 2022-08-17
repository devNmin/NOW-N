import datetime
from dateutil.relativedelta import relativedelta
from multiprocessing import context
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.status import (
    HTTP_201_CREATED
)
from GX.serializers import ConferenceSerializer
from accounts.models import User
from accounts.serializers import UserSerializer
from profiles.serializers import WeightSerializer
from profiles.models import Weight
from trainer.models import Counsel, Member_Coach
from .models import Diet, Diet_Food, Food, Schedule, Training_History
from GX.models import Conference
from .serializers import (
    ConferenceParticipateSerializer,
    CounselHistorySerializer,
    DietFoodSerializer,
    DietSerializer,
    FoodSerializer,
    FoodSimpleSerializer,
    MemberCoachPKSerializer,
    ScheduleSerializer,
    TrainingHistorySerializer,
)

# 식단 정보 한달치 가져오기
@api_view(['GET'])
def diet_month_list(request, current_month):
    diets = Diet.objects.filter(userID=request.user.pk, date__startswith=current_month)
    serializer = DietSerializer(diets, many=True)
    return Response(serializer.data)

# 식단 다이어리 - 오늘의 식단 정보 가져오기
@api_view(['GET'])
def today_diets(request, today_date):
    diets = Diet.objects.filter(userID=request.user.pk, date=today_date)
    serializer = DietSerializer(diets, many=True)
    print("Diets : ", diets)
    foods_list = list()
    for diet in diets:
        print("Diet : ", diet.id)
        foods_data = Diet_Food.objects.filter(diet=diet.id)
        foods_serializer = DietFoodSerializer(data=foods_data, many=True)
        foods_serializer.is_valid()
        foods_list.append(foods_serializer.data)
    print("Foods List : ", foods_list)
    context = {
        'diet_data': serializer.data,
        'foods_data': foods_list,
    }
    return JsonResponse(context)

# 식단 다이어리 - 오늘의 식단 정보 작성하기
@api_view(['POST'])
def create_diets(request):
    # 입력된 식단 정보 저장
    context = {
        'userID': request.data.get('userID'),
        'picture': request.data.get('picture'),
        'category': request.data.get('category'),
        'date': request.data.get('date'),
        'time': request.data.get('time'),
        'comment': request.data.get('comment'),
        'total_calorie': request.data.get('total_calorie'),
        'new_date': request.data.get('new_date'),
    }
    
    # 중복된 시간의 식단 데이터는 삭제처리
    if Diet.objects.filter(userID=request.user.pk, date=request.data.get('date'), time=request.data.get('time')).exists:
        Diet.objects.filter(userID=request.user.pk, date=request.data.get('date'), time=request.data.get('time')).delete()

    serializer = DietSerializer(data=context)

    serializer.is_valid(raise_exception=True)

    serializer.save()

    # 입력된 식단 정보 저장 후 PK 값 추출
    current_diet = get_object_or_404(Diet, userID=request.user.pk, date=request.data.get('date'), time=request.data.get('time'))
    dietPK = current_diet.pk
    print("foods : ", request.data.get('foods'))
    food_list = list()
    for food in request.data.get('foods'):
        current_food = get_object_or_404(Food, name=food.get('name'))
        print('current : ', current_food)
        current_data = {
            'diet': dietPK,
            'food': current_food.id,
            'size': food.get('size'),
            'name': food.get('name'),
        }
        food_list.append(current_data)
    diet_food_serializer = DietFoodSerializer(data=food_list, many=True)

    diet_food_serializer.is_valid(raise_exception=True)
    
    diet_food_serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

# 식단 다이어리 - 식단 정보 삭제
@api_view(['DELETE'])
def delete_diet(request, diet_pk):
    diet = get_object_or_404(Diet, id=diet_pk)
    if diet is None:
        msg = "삭제 실패 : 존재하지 않는 식단입니다."
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    diet.delete()
    msg = "삭제 성공 : 삭제되었습니다."
    return Response(msg, status=status.HTTP_200_OK)


# 식단 다이어리 - 음식 정보 PK로 조회
@api_view(['GET'])
def select_food_by_pk(request, food_pk):
    food = get_object_or_404(Food, pk=food_pk)
    serializer = FoodSerializer(food)
    return Response(serializer.data)
    

# 식단 다이어리 - 음식 정보 이름으로 검색
@api_view(['GET'])
def select_food_by_name(request):
    food_name = request.data.get('name')
    foods = Food.objects.filter(name__contains=food_name)[:5]
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)


# 1:1 코칭룸 - 나의 트레이너 정보 가져오기
@api_view(['GET'])
def mytrainer(request, pk):
    # 자신의 PK로 트레이너 관계인 트레이너 PK 추출
    training = get_object_or_404(Member_Coach, member_id=pk)
    print("내 트레이너 : ", training.coach_id)
    # 트레이너 PK를 이용해 트레이너 정보 가져오기
    trainer = get_object_or_404(User, pk=training.coach_id)
    serializer = UserSerializer(trainer)
    return Response(serializer.data)

# 1:1 코칭룸 - 코칭룸 정보 조회 / 수정
@api_view(['GET', 'PUT'])
def coachingroom(request, pk):
    # 트레이너 PK로 트레이너가 owner인 방 정보 가져오기
    if request.method == 'GET':
        room = get_object_or_404(Conference, owner_id=pk)
        print("Room : ", room)
        serializer = ConferenceSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        room = get_object_or_404(Conference, owner_id=pk)
        serializer = ConferenceSerializer(room, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 1:1 코칭룸 - 코칭룸 On/Off
@api_view(['PUT'])
def coachingroomonoff(request, pk):
    # 트레이너 PK가 owner인 방 is_active를 조회
    room = get_object_or_404(Conference, owner_id=pk)
    # 방이 Off 상태인 경우
    if room.is_active == False:
        context = {
            'is_active': True
        }
        serializer = ConferenceSerializer(room, context, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif room.is_active == True:
        context = {
            'is_active': False
        }
        serializer = ConferenceSerializer(room, context, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 1:1 코칭룸 - 나의 트레이너 1:1 코칭룸 입장
@api_view(['POST'])
def enter_room(request, pk):
    # 자신의 PK로 트레이너 관계인 트레이너 PK 추출
    training = get_object_or_404(Member_Coach, member_id=pk)
    # 트레이너 pk가 owner_id인 방 정보 추출
    conference = get_object_or_404(Conference, owner_id=training.coach_id)
    print("Conference PK : ", conference.pk)
    # 유저 PK를 방 참여 테이블에 추가
    context = {
        'user_id' : pk,
        'conference_id' : conference.pk,
    }
    serializer = ConferenceParticipateSerializer(data=context)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 1:1 코칭룸 - 커뮤니티 (이전 코칭 기록 가져오기)
@api_view(['GET'])
def train_history(request, pk):
    # 회원 PK를 통해 유저-트레이너 관계 PK 찾기
    training = Member_Coach.objects.get(member_id=pk)
    trainingPK = MemberCoachPKSerializer(training)
    # 유저-트레이너 관계 PK를 통해 트레이닝 이력 가져오기
    history = Training_History.objects.get(pk=trainingPK)
    serializer = TrainingHistorySerializer(history)

    return Response(serializer.data)

# 1:1 코칭룸 - 상담이력 (상담이력 가져오기)
@api_view(['GET'])
def counsel_history(request, pk):
    # 회원 PK를 통해 유저-트레이너 관계 PK 찾기
    training = Member_Coach.objects.get(member_id=pk)
    print("아이디 : ", training.id)
    # 유저-트레이너 관계 PK를 통해 상담 이력 찾기
    history = get_object_or_404(Counsel, coaching_id=training.id)
    print("history : ", history)
    context = {
        'id': history.pk,
        'is_exercise': history.is_exercise,
        'is_diet': history.is_diet,
        'times': history.times,
        'start_date': history.start_date,
        'end_date': history.end_date,
        'comment': history.comment,
    }
    serializer = CounselHistorySerializer(data=context)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response("응답실패")

# 1:1 코칭룸 - 스케쥴 (주간 스케쥴 확인 / 스케쥴 추가)
@api_view(['GET', 'POST'])
def schedule_detail(request, pk):
    if request.method == 'GET':
        schedule = get_list_or_404(Schedule, user_id=pk)
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        context = {
            'user_id': pk,
            'day': request.data.get('day'),
            'start_time': request.data.get('start_time'),
            'end_time': request.data.get('end_time'),
        }
        serializer = ScheduleSerializer(data=context)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

# 체중 / 목표 체중 그래프 - 일
@api_view(['GET'])
def weight_graph_day(request):
    weights = Weight.objects.filter(user_id=request.user.id).order_by('-date')[:7]
    serializer = WeightSerializer(weights, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 체중 / 목표 체중 그래프 - 주
@api_view(['GET'])
def weight_graph_week(request):
    # 가장 최근에 저장된 날짜 가져오기
    weights = Weight.objects.filter(user_id=request.user.pk)
    latest = weights.last()
    latest_date = latest.date
    week_data = list()
    week_data.append(latest_date)
    # 1~6주 전 데이터까지 가져오기
    for i in range(1, 6):
        week_date = latest_date - datetime.timedelta(weeks=i)
        week_data.append(week_date)
    week_weights = Weight.objects.filter(date__in=week_data)
    serializer = WeightSerializer(week_weights, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 체중 / 목표 체중 그래프 - 월
@api_view(['GET'])
def weight_graph_month(request):
    # 가장 최근에 저장된 날짜 가져오기
    weights = Weight.objects.filter(user_id=request.user.pk)
    latest = weights.last()
    latest_date = latest.date
    week_data = list()
    week_data.append(latest_date)
    # 1~6달 전 데이터까지 가져오기
    for i in range(1, 6):
        week_date = latest_date - relativedelta(months=i)
        week_data.append(week_date)
    week_weights = Weight.objects.filter(date__in=week_data)
    serializer = WeightSerializer(week_weights, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 칼로리 그래프 - 일
@api_view(['GET'])
def calorie_graph_day(request):
    # 최신 식단 정보 가져오기
    diets = Diet.objects.filter(userID=request.user.pk)
    latest = diets.last()
    latest_date = latest.new_date
    diet_list = Diet.objects.filter(userID=request.user.pk, new_date=latest_date)
    calories = 0
    for a in diet_list:
        calories += a.total_calorie
    calorie_data = list()
    context = {
        'new_date': latest_date,
        'sum_calorie': calories,
    }
    calorie_data.append(context)
    # 1~6일 전 칼로리 정보도 저장
    for i in range(1, 6):
        days_date = latest_date - datetime.timedelta(days=i)
        days_list = Diet.objects.filter(userID=request.user.pk, new_date=days_date)
        days_calorie = 0
        for day in days_list:
            days_calorie += day.total_calorie
        days_data = {
            'new_date': days_date,
            'sum_calorie': days_calorie,
        }
        calorie_data.append(days_data)
    return JsonResponse(calorie_data)
        

# 칼로리 그래프 - 주
@api_view(['GET'])
def calorie_graph_week(request):
    # 최신 식단 정보 가져오기
    diets = Diet.objects.filter(userID=request.user.pk)
    latest = diets.last()
    latest_date = latest.new_date
    diet_list = Diet.objects.filter(userID=request.user.pk, new_date=latest_date)
    calories = 0
    for a in diet_list:
        calories += a.total_calorie
    calorie_data = list()
    context = {
        'new_date': latest_date,
        'sum_calorie': calories,
    }
    calorie_data.append(context)
    # 1~6일 전 칼로리 정보도 저장
    for i in range(1, 6):
        days_date = latest_date - datetime.timedelta(weeks=i)
        days_list = Diet.objects.filter(userID=request.user.pk, new_date=days_date)
        days_calorie = 0
        for day in days_list:
            days_calorie += day.total_calorie
        days_data = {
            'new_date': days_date,
            'sum_calorie': days_calorie,
        }
        calorie_data.append(days_data)
    return JsonResponse(calorie_data)

# 칼로리 그래프 - 월
@api_view(['GET'])
def calorie_graph_month(request):
    # 최신 식단 정보 가져오기
    diets = Diet.objects.filter(userID=request.user.pk)
    latest = diets.last()
    latest_date = latest.new_date
    diet_list = Diet.objects.filter(userID=request.user.pk, new_date=latest_date)
    calories = 0
    for a in diet_list:
        calories += a.total_calorie
    calorie_data = list()
    context = {
        'new_date': latest_date,
        'sum_calorie': calories,
    }
    calorie_data.append(context)
    # 1~6일 전 칼로리 정보도 저장
    for i in range(1, 6):
        days_date = latest_date - relativedelta(months=i)
        days_list = Diet.objects.filter(userID=request.user.pk, new_date=days_date)
        days_calorie = 0
        for day in days_list:
            days_calorie += day.total_calorie
        days_data = {
            'new_date': days_date,
            'sum_calorie': days_calorie,
        }
        calorie_data.append(days_data)
    return JsonResponse(calorie_data)