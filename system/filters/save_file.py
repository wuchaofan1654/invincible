import django_filters
from system.models import SaveFile


class SaveFileFilter(django_filters.rest_framework.FilterSet):
    """
    文件管理 简单过滤器
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    type = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SaveFile
        exclude = ('file',)