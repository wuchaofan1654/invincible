
from system.permissions import CommonPermission
from framework.filters import DataLevelPermissionsFilter
from framework.viewsets import CustomModelViewSet
from custom.filters import CheckResultFilter
from custom.models import CheckResult
from custom.serializers import CheckResultSerializer, CheckResultCreateUpdateSerializer


class CheckResultModelViewSet(CustomModelViewSet):
    """
    检查结果模型 的CRUD视图
    """
    queryset = CheckResult.objects.all()
    serializer_class = CheckResultSerializer
    create_serializer_class = CheckResultCreateUpdateSerializer
    update_serializer_class = CheckResultCreateUpdateSerializer
    filter_class = CheckResultFilter
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('check_status',)
    ordering = 'create_datetime'  # 默认排序
