
from framework.filters import DataLevelPermissionsFilter
from framework.viewsets import CustomModelViewSet
from system.permissions import CommonPermission
from system.filters import DictDataFilter
from system.models import DictData
from system.serializers import DictDataSerializer, DictDataCreateUpdateSerializer, ExportDictDataSerializer


class DictDataModelViewSet(CustomModelViewSet):
    """
    字典管理模型的CRUD视图
    """
    queryset = DictData.objects.all()
    serializer_class = DictDataSerializer
    create_serializer_class = DictDataCreateUpdateSerializer
    update_serializer_class = DictDataCreateUpdateSerializer
    # list_serializer_class = ListRoleSerializer
    # retrieve_serializer_class = DetailRoleSerializer
    extra_filter_backends = [DataLevelPermissionsFilter]
    filter_class = DictDataFilter
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('dictName',)
    ordering = 'id'  # 默认排序
    export_field_data = ['字典主键', '字典名称', '字典类型', '字典状态', '创建者', '修改者', '备注']
    export_serializer_class = ExportDictDataSerializer

