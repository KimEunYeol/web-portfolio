from django.urls import path, include
from django.contrib.auth import views as UserViews

from .views import signup, signup_idcheck, signup_result, signup_completed, error, UserLoginView, UserMypageView, UserPasswordChangedView


urlpatterns = [
    path('signup/', signup, name='signup'),
	path('signup_idcheck/', signup_idcheck, name='signup_idcheck'),
	path('signup_result/', signup_result, name='signup_result'),
	path('signup_result/signup_completed/', signup_completed, name='signup_completed'),
    path('signup_result/signup_error/', error, name='signup_error'),

    path('login/', UserLoginView.as_view(), name='login'),
	path('logout/', UserViews.LogoutView.as_view(), name='logout'),
	path('mypage/', UserMypageView.as_view(), name='mypage'),
	path('password_change_done/', UserPasswordChangedView.as_view(), name='password_change_done'),

]