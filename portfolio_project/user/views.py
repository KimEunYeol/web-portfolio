import math

from django.shortcuts import render, redirect
from django.db.models import Count
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView, TemplateView 
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from .models import User, UserManager


class UserLoginView(LoginView):
    template_name = 'user/login.html'

class UserMypageView(PasswordChangeView):
	template_name = 'user/mypage.html'

class UserPasswordChangedView(PasswordChangeDoneView):
	template_name = 'user/password_change_done.html'

def signup(request):
	return render(request, 'user/signup.html')


def signup_idcheck(request):
	if request.method == "POST":
		username = request.POST['username']
	else:
		username = ''

	idObject = User.objects.filter(username__exact=username)
	idCount = idObject.count()

	if idCount > 0:
		msg = "<font color='#00c1f2'>이미 존재하는 ID입니다.</font><input type='hidden' name='IDCheckResult' id='IDCheckResult' value=0 />"
	else:
		msg = "<font color= '#00c1f2'>사용할 수 있는 ID입니다.</font><input type='hidden' name='IDCheckResult' id='IDCheckResult' value=1 />"

	return HttpResponse(msg)


def signup_result(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		name = request.POST['name']
		phone = request.POST['phone']
		email = request.POST['email']

	try:
		if username and User.objects.filter(username__exact=username).count() == 0:
			user = User.objects.create_user(
				username, password, name, email, phone
			)
			redirection_page = 'signup_completed/'
		else:
			redirection_page = 'signup_error/'
	except:
		redirection_page = 'signup_error/'

	return redirect(redirection_page)


def signup_completed(request):
	return render(request, 'user/signup_completed.html')


def error(request):
    return render(request, 'error.html')
