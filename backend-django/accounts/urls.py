from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView


urlpatterns = [
    path('signup/', RegistrationAPIView.as_view()),

    path('login/', LoginAPIView.as_view()),

    path('current/', UserRetrieveUpdateAPIView.as_view()),
]