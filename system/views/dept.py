from rest_framework.request import Request

from framework.response import SuccessResponse
from system.permissions import CommonPermission, DeptDestroyPermission
from framework.filters import DataLevelPermissionsFilter
from framework.viewsets import CustomModelViewSet
from system.filters import DeptFilter
from system.models import Dept
from system.serializers import DeptSerializer, DeptCreateUpdateSerializer, DeptTreeSerializer


class DeptModelViewSet(CustomModelViewSet):
    """
    部门管理 的CRUD视图
    """
    queryset = Dept.objects.all()
    serializer_class = DeptSerializer
    create_serializer_class = DeptCreateUpdateSerializer
    update_serializer_class = DeptCreateUpdateSerializer
    filter_class = DeptFilter
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission, DeptDestroyPermission)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('deptName',)
    ordering = 'create_datetime'  # 默认排序

    def exclude_list(self, request: Request, *args, **kwargs):
        """
        过滤剔除同级部门
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        dept_queryset = Dept.objects.filter(id=kwargs.get('pk')).first()
        parentId = dept_queryset.parentId if dept_queryset else ''
        queryset = self.queryset.exclude(parentId=parentId).order_by('orderNum')
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        serializer = self.get_serializer(queryset, many=True)
        return SuccessResponse(serializer.data)

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
        serializer = DeptTreeSerializer(queryset, many=True)
        return SuccessResponse(serializer.data)

    def role_dept_tree_select(self, request: Request, *args, **kwargs):
        """
        根据角色ID查询部门树结构
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        dept_queryset = Dept.objects.filter(role__id=kwargs.get('pk')).values_list('id', flat=True)
        queryset = self.filter_queryset(self.get_queryset())
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        serializer = DeptTreeSerializer(queryset, many=True)
        return SuccessResponse({
            'depts': serializer.data,
            'checkedKeys': dept_queryset
        })

