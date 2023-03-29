import django_filters
from system.models import Menu


class MenuFilter(django_filters.rest_framework.FilterSet):
    """
    菜单管理 简单序过滤器
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Menu
        exclude = ('description', 'creator', 'modifier')

