from django.urls import path

from .views import blog, guest_book


urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/guestbook', guest_book, name='guestbook'),
]