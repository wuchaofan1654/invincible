import django_filters
from system.models import DictData


class DictDataFilter(django_filters.rest_framework.FilterSet):
    """
    字典管理 简单过滤器
    """
    dictName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = DictData
        fields = '__all__'
