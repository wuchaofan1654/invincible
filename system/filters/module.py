import django_filters

from system.models import Module


class ModuleFilter(django_filters.rest_framework.FilterSet):
    """
    模块管理 简单序过滤器
    """
    moduleName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Module
        fields = '__all__'
