import django_filters
from system.models import DictDetails


class DictDetailsFilter(django_filters.rest_framework.FilterSet):
    """
    字典详情 简单过滤器
    """
    dictLabel = django_filters.CharFilter(lookup_expr='icontains')
    dictType = django_filters.CharFilter(field_name='dict_data__dictType')

    class Meta:
        model = DictDetails
        fields = '__all__'
