from django.shortcuts import render


def guest_book(request):
    return render(request, 'guestbook/guestbook.html', context=None)
