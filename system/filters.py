import django_filters
from django.contrib.auth import get_user_model

from system.models import Menu, Dept, Post, Role, Module
from utils.model_util import get_dept
from system.models import DictDetails, DictData, ConfigSettings, MessagePush, SaveFile
from system.models import LoginInfo, OperationLog, CeleryLog


UserProfile = get_user_model()


class MenuFilter(django_filters.rest_framework.FilterSet):
    """
    菜单管理 简单序过滤器
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Menu
        exclude = ('description', 'creator', 'modifier')


class DeptFilter(django_filters.rest_framework.FilterSet):
    """
    部门管理 简单序过滤器
    """
    deptName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Dept
        exclude = ('description', 'creator', 'modifier')


class ModuleFilter(django_filters.rest_framework.FilterSet):
    """
    模块管理 简单序过滤器
    """
    moduleName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Module
        fields = '__all__'


class PostFilter(django_filters.rest_framework.FilterSet):
    """
    岗位管理 简单序过滤器
    """
    postName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        exclude = ('description', 'creator', 'modifier')


class RoleFilter(django_filters.rest_framework.FilterSet):
    """
    角色管理 简单序过滤器
    """
    roleName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Role
        exclude = ('description', 'creator', 'modifier')


class UserProfileFilter(django_filters.rest_framework.FilterSet):
    """
    用户管理 简单序过滤器
    """
    username = django_filters.CharFilter(lookup_expr='icontains')
    mobile = django_filters.CharFilter(lookup_expr='icontains')
    print("")
    deptId = django_filters.CharFilter(method='filter_deptId')

    @classmethod
    def filter_deptId(cls, queryset, name, value):
        return queryset.filter(dept__id__in=get_dept(dept_id=value))

    class Meta:
        model = UserProfile
        exclude = ('secret', 'password', 'avatar')


class DictDataFilter(django_filters.rest_framework.FilterSet):
    """
    字典管理 简单过滤器
    """
    dictName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = DictData
        fields = '__all__'


class DictDetailsFilter(django_filters.rest_framework.FilterSet):
    """
    字典详情 简单过滤器
    """
    dictLabel = django_filters.CharFilter(lookup_expr='icontains')
    dictType = django_filters.CharFilter(field_name='dict_data__dictType')

    class Meta:
        model = DictDetails
        fields = '__all__'


class ConfigSettingsFilter(django_filters.rest_framework.FilterSet):
    """
    参数设置 简单过滤器
    """
    configName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ConfigSettings
        fields = '__all__'


class SaveFileFilter(django_filters.rest_framework.FilterSet):
    """
    文件管理 简单过滤器
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    type = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SaveFile
        exclude = ('file',)





class LoginInforFilter(django_filters.rest_framework.FilterSet):
    """
    登录日志 简单过滤器
    """
    loginLocation = django_filters.CharFilter(lookup_expr='icontains')
    userName = django_filters.CharFilter(field_name='creator__username', lookup_expr='icontains')

    class Meta:
        model = LoginInfo
        fields = '__all__'


class OperationLogFilter(django_filters.rest_framework.FilterSet):
    """
    操作日志 简单过滤器
    """
    request_modular = django_filters.CharFilter(lookup_expr='icontains')
    creator_username = django_filters.CharFilter(field_name='creator__username', lookup_expr='icontains')

    class Meta:
        model = OperationLog
        fields = '__all__'


class CeleryLogFilter(django_filters.rest_framework.FilterSet):
    """
    定时日志 简单过滤器
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    func_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CeleryLog
        fields = '__all__'

