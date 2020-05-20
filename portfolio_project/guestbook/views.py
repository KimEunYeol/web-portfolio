import math

from django.shortcuts import render, redirect
from django.db.models import Count
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from datetime import datetime
from .models import GuestBook, Comment, Like


def guest_book(request):
    return render(request, 'guestbook/guestbook.html', context=None)

@login_required(None,'','/user/login/')
def guestbook_list(request):
	error_flag = False

	if request.method == "POST":
		title = request.POST.get('title', False)
		content = request.POST.get('content', '')

		try:
			img_file = request.FILES['img_file']
		except:
			img_file = None

		try:
			if request.user and title and content:
				guestbook_post = GuestBook(username=request.user, title=title, content=content, image=img_file)
				guestbook_post.save()
			else:
				error_flag = True
		except:
			error_flag = True

	guestbook_posts = GuestBook.objects.all().order_by('-id')
	
	args = {}
	args.update({"error_flag": error_flag})
	args.update({"guestbook_posts":guestbook_posts})

	return render(request, 'guestbook/guestbook_list.html', args)


class GuestBookView(DetailView):
	model = GuestBook
	template_name = 'guestbook/guestbook_view.html'

class GuestBookModifyView(DetailView):
	model= GuestBook
	template_name = 'guestbook/guestbook_modify.html'


def guestbook_write_result(request):
	if request.method == "POST":
		title = request.POST['title']
		content = request.POST['content']
		try:
			img_file = request.FILES['img_file']
		except:
			img_file = None
	else:
		title = None

	args={}

	try:
		if request.user and title and content:
			guestbook_post  = GuestBook(username=request.user, title=title, content=content, image=img_file)
			guestbook_post .save()
			redirect('/guestbook/list/')
		else:
			redirect('/guestbook/guestbook_error/')
	except:
		redirect('/guestbook/guestbook_error/')

	return redirect('/guestbook/list/')


def guestbook_modify_result(request):
	if request.method == "POST":
		title = request.POST['title']
		content = request.POST['content']
		guestbook_post_id = request.POST['id']

		try:
			img_file = request.FILES['img_file']
		except:
			img_file = None
	else:
		title = None

	args={}

	try:
		guestbook_post = GuestBook.objects.get(id=guestbook_post_id)
		if request.user and title and content and guestbook_post_id:
			
			if guestbook_post.username != request.user:
				redirect('/guestbook/guestbook_error/')
				# error flag를 만들어줘보자
			else:
				guestbook_post.title=title
				guestbook_post.content=content
				guestbook_post.modify_dt=timezone.now()
				
				if img_file:
					article.image = img_file

				guestbook_post.save()
				redirection_page = '/guestbook/view/' + guestbook_post_id + '/'

		else:
			redirect('/guestbook/guestbook_error/')

	except:
		redirect('/guestbook/guestbook_error/')

	return redirect(redirection_page)



def guestbook_delete_result(request):
	if request.method == "POST":
		guestbook_post_id = request.POST['guestbook_post_id']
	else:
		guestbook_post_id = -1

	args={}
	guestbook_post = GuestBook.objects.get(id=guestbook_post_id)

	if  request.user == guestbook_post.username:
		guestbook_post.delete()
		redirect('/guestbook/list/')
	else:
		redirect('/guestbook/guestbook_error/')

	return redirect('/guestbook/list/')


def comment_list(request, guestbook_post):
	comments = Comment.objects.filter(guestbook_post__id=guestbook_post).order_by('reference_comment_id','level','id')

	args = {}
	args.update({"comments":comments})

	return render(request, 'guestbook/comment_list.html', args)

class CommentModifyView(DetailView):
	model = Comment

	template_name = 'guestbook/comment_modify.html'


def comment_write_result(request):
	if request.method == "POST":
		content = request.POST['content']
		level = request.POST['level']
		id = request.POST['id']
	else:
		content = None

	args={}

	try:
		if request.user and content and id:
			if level == "0":
				guestbook_post = GuestBook.objects.get(id=id)
				comment = Comment(guestbook_post=guestbook_post, username=request.user, level=level, content=content)
				comment.save()
				comment.reference_comment_id=comment.id
				comment.save()
				redirection_page = '/guestbook/comment/list/' + id + '/'

			else:
				guestbook_post = Comment.objects.get(id=id).guestbook_post
				comment = Comment(guestbook_post=guestbook_post, username=request.user, level=level, content=content, reference_comment_id=id)
				comment.save()
				redirection_page = '/guestbook/comment/list/' + str(guestbook_post.id) + '/'

		else:
			redirect('/guestbook/guestbook_error/')

	except:
		redirect('/guestbook/guestbook_error/')

	return redirect(redirection_page)


def comment_modify_result(request):
	if request.method == "POST":
		content = request.POST['content']
		comment_id = request.POST['id']
	else:
		content = None

	try:
		if request.user and content and comment_id:
			comment = Comment.objects.get(id=comment_id)
			comment.content = content
			comment.save()
			
			redirection_page = '/guestbook/comment/list/' + str(comment.guestbook_post.id) + '/'

		else:
			redirect('/guestbook/guestbook_error/')
	except:
		redirect('/guestbook/guestbook_error/')

	return redirect(redirection_page)


def comment_delete_result(request):
	if request.method == "POST":
		comment_id = request.POST['comment_id']
	else:
		comment_id = -1

	comment = Comment.objects.get(id=comment_id)

	if request.user == comment.username:
		comment.delete()
		redirection_page = '/guestbook/comment/list/' + str(comment.guestbook_post.id) + '/'

	else:
		redirect('/guestbook/guestbook_error/')

	return redirect(redirection_page)

def guestbook_like(request, guestbook_post):
	args={}

	like_count = Like.objects.filter(guestbook_post__id=guestbook_post).count()
	user_count = Like.objects.filter(guestbook_post__id=guestbook_post).filter(username=request.user).count()

	args.update({"like_count": like_count})
	args.update({"user_count": user_count})
	args.update({"guestbook_post_id": guestbook_post})

	return render(request, 'guestbook/guestbook_like.html', args)

def guestbook_like_result(request):
	if request.method == "POST":
		guestbook_post_id = request.POST['guestbook_post_id']
	else:
		guestbook_post_id = -1

	guestbook_post = GuestBook.objects.get(id=guestbook_post_id)
	like_confirm = Like.objects.filter(guestbook_post=guestbook_post)
	like_already_click = like_confirm.filter(username=request.user).count()

	args = {}
	if guestbook_post.username == request.user:
		args.update({"like_err_msg":"본인의 게시물에는 추천할 수 없습니다"})
	elif like_already_click == 1:
		args.update({"like_err_msg":"이미 추천하였습니다"})
	else:
		like = Like(guestbook_post=guestbook_post, username=request.user)
		like.save()

	args.update({"guestbook_post_id":guestbook_post_id})

	return JsonResponse(args)

def error(request):
    return render(request, 'guestbook/error.html')