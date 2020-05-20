from django.urls import path, re_path
from .views import PostListView, PostDetailView, TagCloudTemplateView, TaggedObjectListView, SearchFormView


urlpatterns = [
    path('', PostListView.as_view(), name='post_index'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('tag/', TagCloudTemplateView.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', TaggedObjectListView.as_view(), name='tagged_object_list'),
    path('search/', SearchFormView.as_view(), name='search'),
]