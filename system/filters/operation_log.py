import django_filters
from system.models import OperationLog


class OperationLogFilter(django_filters.rest_framework.FilterSet):
    """
    操作日志 简单过滤器
    """
    request_modular = django_filters.CharFilter(lookup_expr='icontains')
    creator_username = django_filters.CharFilter(field_name='creator__username', lookup_expr='icontains')

    class Meta:
        model = OperationLog
        fields = '__all__'
