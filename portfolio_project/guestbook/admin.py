from django.contrib import admin
from .models import GuestBook, Comment, Like
    
    
admin.site.register(GuestBook)
admin.site.register(Comment)
admin.site.register(Like)