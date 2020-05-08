from django.urls import path

from .views import (
    guestbook_list, GuestBookView, GuestBookModifyView, guestbook_delete_result, guestbook_modify_result,
    comment_list, CommentModifyView, comment_write_result, comment_modify_result, comment_delete_result,
    guestbook_like, guestbook_like_result, error, guest_book
)

urlpatterns = [
    path('', guestbook_list, name='guestbook'),
    path('list/', guestbook_list, name='guestbook_list'),
	path('view/<int:pk>/', GuestBookView.as_view(), name='guestbook_view'),
	path('modify/<int:pk>/', GuestBookModifyView.as_view(), name='guestbook_modify'),
	path('guestbook_delete_result/', guestbook_delete_result, name='guestbook_delete_result'),
	path('guestbook_modify_result/', guestbook_modify_result, name='guestbook_modify_result'),

	path('comment/list/<guestbook_post>/', comment_list, name='comment_list'),
	path('comment/modify/<int:pk>/', CommentModifyView.as_view(), name='comment_modify'),
	path('comment_write_result/', comment_write_result, name='comment_write_result'),
	path('comment_modify_result/', comment_modify_result, name='comment_modify_result'),
	path('comment_delete_result/', comment_delete_result, name='comment_delete_result'),
	
	path('like/<int:guestbook_post>/', guestbook_like, name='guestbook_like'),
	path('like_result/', guestbook_like_result, name='guestbook_like_result'),

    path('guestbook_error/', error, name='guestbook_error'),

]