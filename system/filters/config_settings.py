import django_filters
from system.models import ConfigSettings


class ConfigSettingsFilter(django_filters.rest_framework.FilterSet):
    """
    参数设置 简单过滤器
    """
    configName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ConfigSettings
        fields = '__all__'
