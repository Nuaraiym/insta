from django_filters.rest_framework import FilterSet

from .models import PostLike,Post

class PostLikeFilter(FilterSet):
    class Meta:
        model = PostLike
        fields = {
            'post' : ['exact'],
            'created_at': ['gt','lt']
        }

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'hashtag' : ['exact'],

        }