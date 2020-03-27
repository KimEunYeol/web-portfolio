from django.shortcuts import render


def index(request):
    return render(request, 'intro/index.html', context=None)

def about(request):
    return render(request, 'intro/about.html', context=None)

def project(request):
    return render(request, 'intro/project.html', context=None)