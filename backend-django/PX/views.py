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
from .models import Diet, Food, Schedule, Training_History
from GX.models import Conference
from .serializers import (
    ConferenceParticipateSerializer,
    CounselHistorySerializer,
    DietFoodSerializer,
    DietSerializer,
    FoodSerializer,
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
    return Response(serializer.data)

# 식단 다이어리 - 오늘의 식단 정보 작성하기
@api_view(['POST'])
def create_diets(request):
    # 들어온 식단 정보 저장
    serializer = DietSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # 들어온 식단 정보 중 음식 정보를 Diet와 관계 매핑
        dietPK = serializer.data.get('pk')
        for food in serializer.foods:
            foodPK = food.food_pk
            size = food.food_size
            context = {
                'diet': dietPK,
                'food': foodPK,
                'size': size
            }
            dfs = DietFoodSerializer(data=context)
            if dfs.is_valid():
                dfs.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

# 식단 다이어리 - 음식 정보 PK로 조회
@api_view(['GET'])
def select_food_by_pk(request, food_pk, food_size):
    food = get_object_or_404(Food, pk=food_pk)
    fs = FoodSerializer(food)
    multiple = food_size / fs.data.get('serving_size')
    context = {
        'id': food_pk,
        'category': fs.data.get('category'),
        'name': fs.data.get('name'),
        'serving_size': food_size,
        'unit': fs.data.get('unit'),
        'kcal': fs.data.get('kcal') * multiple,
        'water': fs.data.get('water') * multiple,
        'protein': fs.data.get('protein') * multiple,
        'fat': fs.data.get('fat') * multiple,
        'carbohydrate': fs.data.get('carbohydrate') * multiple,
        'sugar': fs.data.get('sugar') * multiple,
        'glucose': fs.data.get('glucose') * multiple,
        'calcium': fs.data.get('calcium') * multiple,
        'natrium': fs.data.get('natrium') * multiple,
    }
    serializer = FoodSerializer(context)
    return Response(serializer.data)
    

# 식단 다이어리 - 음식 정보 이름으로 검색
@api_view(['GET'])
def select_food_by_name(reqeust, food_name):
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
    # 식단 정보 가져오기
    diets = Diet.objects.filter(userID=request.user.pk)
    latest_diet = diets.last()
    latest_diet.date
    diet_list = list()
    diet_list.append(latest_diet.date)
    print("diet_list : ", diet_list)
    pass
        

# 칼로리 그래프 - 주
@api_view(['GET'])
def calorie_graph_week(request):
    pass

# 칼로리 그래프 - 월
@api_view(['GET'])
def calorie_graph_month(request):
    pass

# 영양소 그래프 - 일
@api_view(['GET'])
def nutrient_graph_day(request):
    pass

# 영양소 그래프 - 주
@api_view(['GET'])
def nutrient_graph_week(request):
    pass

# 영양소 그래프 - 월
@api_view(['GET'])
def nutrient_graph_month(request):
    pass