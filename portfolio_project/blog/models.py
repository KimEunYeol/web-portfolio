from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from user.models import User
from django.utils.text import slugify


class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='username')
    title = models.CharField(verbose_name='Title', max_length=64, blank=False)
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(blank=True, null=True)
    tags = TaggableManager(blank=True)
    create_dt = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
    modify_dt = models.DateTimeField(verbose_name='Modify date', auto_now=True)


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'post'
        db_table = 'blog_post'
        ordering = ('-modify_dt',)

    def __str__(self):
        return '%s - %s' % (self.id, self.title)

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.id,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
