from django.shortcuts import render


def signup(request):
    return render(request, 'user/signup.html', context=None)

def login(request):
    return render(request, 'user/login.html', context=None)

def mypage(request):
    return render(request, 'user/mypage.html', context=None)