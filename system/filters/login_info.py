import django_filters
from system.models import LoginInfo


class LoginInforFilter(django_filters.rest_framework.FilterSet):
    """
    登录日志 简单过滤器
    """
    loginLocation = django_filters.CharFilter(lookup_expr='icontains')
    userName = django_filters.CharFilter(field_name='creator__username', lookup_expr='icontains')

    class Meta:
        model = LoginInfo
        fields = '__all__'
