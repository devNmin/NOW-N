from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import (
    RegistrationAPIView,
    LoginAPIView,
    UserRetrieveUpdateAPIView,
    ChangePasswordView,
    LogoutAPIView,
    DeleteUserView,
)

app_name = 'accounts'

urlpatterns = [
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('token_verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('signup/', RegistrationAPIView.as_view()),

    path('login/', LoginAPIView.as_view(), name="login"),

    path('logout/', LogoutAPIView.as_view(), name="logout"),

    path('current/', UserRetrieveUpdateAPIView.as_view(), name="current"),

    path('change_pw/<int:pk>/', ChangePasswordView.as_view(), name='change_pw'),

    path('delete/<int:pk>/', DeleteUserView.as_view() , name="delete"),
]