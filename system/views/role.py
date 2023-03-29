
from system.permissions import CommonPermission
from framework.filters import DataLevelPermissionsFilter
from framework.viewsets import CustomModelViewSet
from system.filters import RoleFilter
from system.models import Role
from system.serializers import RoleSerializer, RoleCreateUpdateSerializer, ExportRoleSerializer


class RoleModelViewSet(CustomModelViewSet):
    """
    角色管理 的CRUD视图
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    create_serializer_class = RoleCreateUpdateSerializer
    update_serializer_class = RoleCreateUpdateSerializer
    filter_class = RoleFilter
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('roleName',)
    ordering = 'create_datetime'  # 默认排序
    export_field_data = ['角色序号', '角色名称', '角色权限', '角色排序', '数据范围', '角色状态', '创建者', '修改者', '备注']
    export_serializer_class = ExportRoleSerializer
