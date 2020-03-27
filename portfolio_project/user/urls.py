from django.urls import path

from .views import signup, login, mypage


urlpatterns = [
    path('user/signup', signup, name='signup'),
    path('user/login', login, name='login'),
    path('user/mypage', mypage, name='mypage'),
]