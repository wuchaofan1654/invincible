import django_filters
from system.models import Post


class PostFilter(django_filters.rest_framework.FilterSet):
    """
    岗位管理 简单序过滤器
    """
    postName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        exclude = ('description', 'creator', 'modifier')