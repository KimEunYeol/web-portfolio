from django.urls import path

from .views import guest_book


urlpatterns = [
    path('', guest_book, name='guestbook'),
]