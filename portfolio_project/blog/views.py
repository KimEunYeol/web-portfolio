from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.conf import settings
from django.db.models import Q

from .models import Post
from .forms import PostSearchForm

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.title}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.title}"
        return context

class TagCloudTemplateView(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectListView(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context


class SearchFormView(FormView): 
    form_class = PostSearchForm 
    template_name = 'blog/post_search.html' 

    def form_valid(self, form): 
        searchWord = form.cleaned_data['search_word']
        # 왜래키는 __fieldname을 한번더 추가해줘야한다
        post_search_list = Post.objects.filter(Q(title__icontains=searchWord) |  Q(content__icontains=searchWord) | Q(username__username__icontains=searchWord)).distinct()

        context = {} 
        context['form'] = form 
        context['search_term'] = searchWord
        context['object_list'] = post_search_list 

        return render(self.request, self.template_name, context)
