from django.shortcuts import render


def blog(request):
    return render(request, 'blog/blog.html', context=None)

def guest_book(request):
    return render(request, 'blog/guestbook.html', context=None)
