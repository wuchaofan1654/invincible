import django_filters
from system.models import CeleryLog


class CeleryLogFilter(django_filters.rest_framework.FilterSet):
    """
    定时日志 简单过滤器
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    func_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CeleryLog
        fields = '__all__'
