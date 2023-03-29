import django_filters
from system.models import Role


class RoleFilter(django_filters.rest_framework.FilterSet):
    """
    角色管理 简单序过滤器
    """
    roleName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Role
        exclude = ('description', 'creator', 'modifier')