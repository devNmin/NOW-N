from multiprocessing import context

from GX.serializers import ConferenceSerializer
from .models import User
from django.contrib.auth import authenticate
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import (
    RegisterUserSerializer,
    LoginSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    RefreshTokenSerializer,
    )


# 회원가입
class RegistrationAPIView(APIView):
    permission_classes = [ AllowAny ]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # 트레이너 가입 시 1:1 코칭 룸 생성, 할당
            if serializer.data.get('grade') == '트레이너':
                context = {
                    'owner_id': serializer.data.get('id'),
                    'password': 1111,
                    'category': 5,
                    'title': serializer.data.get('name'),
                    'description': '1:1 코칭룸입니다.',
                    'max_user': 2,
                    'thumnail': 'https://ibb.co/qg4XZZP',
                    'is_active': False,
                }
                conference = ConferenceSerializer(data=context)
                if conference.is_valid():
                    conference.save()
            if user:
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그인
class LoginAPIView(APIView):
    permission_classes = [ AllowAny ]

    def post(self, request):
        user_id = request.data.get('user_id')
        password = request.data.get('password')

        if user_id is None:
            return Response("아이디를 입력하세요.")

        if password is None:
            return Response("비밀번호를 입력하세요.")

        user = authenticate( 
            user_id=user_id, 
            password=password
        )

        if user:
            login_serializer = LoginSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            response = Response(
                {
                    "user": login_serializer.data,
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return response

        if user is None:
            return Response("로그인에 실패하였습니다.", status=status.HTTP_400_BAD_REQUEST)


# 회원정보 조회 / 수정
class UserRetrieveUpdateAPIView(APIView):
        permission_classes = (IsAuthenticated,)
        serializer_class = UserSerializer
        

        def get(self, request, *args, **kwargs):

            serializer = self.serializer_class(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        def put(self, request, *args, **kwargs):
            serializer_data = request.data

            serializer = self.serializer_class(
                request.user, data=serializer_data, partial=True
            )
            
            serializer.is_valid(raise_exception=True)

            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)


# 비밀번호 변경
class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [ IsAuthenticated ]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'message': 'Password updated successfully',
            }
            return Response(response, status=status.HTTP_200_OK,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그아웃
class LogoutAPIView(generics.GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response("로그아웃 되었습니다.", status=status.HTTP_204_NO_CONTENT)


# 회원탈퇴
class DeleteUserView(APIView):
    permission_classes = [ IsAuthenticated ]

    def delete(self, request, **kwargs):
        if kwargs.get('pk') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            pk = kwargs.get('pk')
            user_object = User.objects.get(id=pk)
            user_object.delete()
            return Response("delete ok", status=status.HTTP_200_OK)
