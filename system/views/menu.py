from django.contrib.auth import authenticate, get_user_model
from rest_framework.request import Request
from rest_framework.views import APIView

from framework.response import SuccessResponse, ErrorResponse
from apps.permission.permissions import CommonPermission, DeptDestroyPermission
from frames.filters import DataLevelPermissionsFilter
from frames.viewsets import CustomModelViewSet
from apps.permission.filters import MenuFilter, DeptFilter, PostFilter, RoleFilter, UserProfileFilter, ModuleFilter
from apps.permission.models import Role, Menu, Dept, Post, Module
from apps.permission.serializers import UserProfileSerializer, MenuSerializer, RoleSerializer, \
    MenuCreateUpdateSerializer, DeptSerializer, DeptCreateUpdateSerializer, PostSerializer, PostCreateUpdateSerializer, \
    RoleCreateUpdateSerializer, DeptTreeSerializer, MenuTreeSerializer, UserProfileCreateUpdateSerializer, \
    PostSimpleSerializer, RoleSimpleSerializer, ExportUserProfileSerializer, ExportRoleSerializer, ExportPostSerializer, \
    UserProfileImportSerializer, ModuleSerializer, ModuleTreeSerializer, ModuleCreateUpdateSerializer
from apps.system.models import DictDetails


class MenuModelViewSet(CustomModelViewSet):
    """
    菜单模型 的CRUD视图
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    create_serializer_class = MenuCreateUpdateSerializer
    update_serializer_class = MenuCreateUpdateSerializer
    filter_class = MenuFilter
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('name',)
    ordering = 'create_datetime'  # 默认排序

    def tree_select_list(self, request: Request, *args, **kwargs):
        """
        递归获取部门树
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = self.filter_queryset(self.get_queryset())
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        serializer = MenuTreeSerializer(queryset, many=True)
        return SuccessResponse(serializer.data)

    def role_menu_tree_select(self, request: Request, *args, **kwargs):
        """
        根据角色ID查询菜单下拉树结构
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        menu_queryset = Menu.objects.filter(role__id=kwargs.get('pk')).values_list('id', flat=True)
        queryset = self.filter_queryset(self.get_queryset())
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        serializer = MenuTreeSerializer(queryset, many=True)
        return SuccessResponse({
            'menus': serializer.data,
            'checkedKeys': menu_queryset
        })

