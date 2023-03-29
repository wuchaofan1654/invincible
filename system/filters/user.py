import django_filters
from django.contrib.auth import get_user_model
from utils.model_util import get_dept


UserProfile = get_user_model()


class UserProfileFilter(django_filters.rest_framework.FilterSet):
    """
    用户管理 简单序过滤器
    """
    username = django_filters.CharFilter(lookup_expr='icontains')
    mobile = django_filters.CharFilter(lookup_expr='icontains')
    dept_id = django_filters.CharFilter(method='filter_dept_id')

    @classmethod
    def filter_dept_id(cls, queryset, name, value):
        print(queryset)
        return queryset.filter(dept__id__in=get_dept(dept_id=value))

    class Meta:
        model = UserProfile
        exclude = ('secret', 'password', 'avatar')
