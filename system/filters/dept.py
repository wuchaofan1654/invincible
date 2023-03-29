import django_filters
from system.models import Dept


class DeptFilter(django_filters.rest_framework.FilterSet):
    """
    部门管理 简单序过滤器
    """
    deptName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Dept
        exclude = ('description', 'creator', 'modifier')
