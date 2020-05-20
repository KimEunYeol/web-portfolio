from django.db import models
from django.utils import timezone
from user.models import User


class GuestBook(models.Model):
	username = models.ForeignKey(User, models.DO_NOTHING, verbose_name='username')
	title = models.CharField(verbose_name='Title', max_length=64, blank=False)
	content = models.TextField(verbose_name='Content')
	image = models.ImageField(blank=True, null=True)

	create_dt = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
	modify_dt = models.DateTimeField(verbose_name='Modify date', auto_now=True)

	def __str__(self):
		return '[%d] %.40s' % (self.id, self.title)

	class Meta:
		verbose_name = 'guestbook'
		verbose_name_plural = 'guestbook'
		db_table = 'guestbook'


class Comment(models.Model):
	guestbook_post = models.ForeignKey(GuestBook, models.DO_NOTHING)
	username = models.ForeignKey(User, models.DO_NOTHING, verbose_name='username')
	level = models.IntegerField(blank=True, null=True)
	content = models.TextField(verbose_name='Contnet')
	reference_comment_id = models.IntegerField(blank=True, null=True)

	create_dt = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
	modify_dt = models.DateTimeField(verbose_name='Modify date', auto_now=True)

	def __str__(self):
		return '[%d] %.40s - [%d] %.40s' % (self.guestbook_post.id, self.guestbook_post.title, self.id, self.content)

	class Meta:
		verbose_name = 'comment'
		verbose_name_plural = 'comment'
		db_table = 'comment'

class Like(models.Model):
	guestbook_post = models.ForeignKey(GuestBook, models.DO_NOTHING)
	username = models.ForeignKey(User, models.DO_NOTHING, verbose_name='username')

	def __str__(self):
		return '[%d] %.40 - %s' % (self.guestbook_post.id, self.guestbook_post.title, self.username.name)

	class Meta:
		verbose_name = 'like'
		verbose_name_plural = 'like'
		db_table = 'like'