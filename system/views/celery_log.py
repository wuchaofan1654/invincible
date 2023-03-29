
from rest_framework.request import Request

from framework.filters import DataLevelPermissionsFilter
from framework.response import SuccessResponse
from framework.viewsets import CustomModelViewSet
from system.permissions import CommonPermission
from system.filters import CeleryLogFilter
from system.models import CeleryLog
from system.serializers import CeleryLogSerializer, ExportCeleryLogSerializer


class CeleryLogModelViewSet(CustomModelViewSet):
    """
   定时任务日志 模型的CRUD视图
   """
    queryset = CeleryLog.objects.all()
    serializer_class = CeleryLogSerializer
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    filter_class = CeleryLogFilter
    ordering = '-create_datetime'  # 默认排序
    export_field_data = ['任务名称', '执行参数', '执行时间', '运行状态', '任务结果', '创建时间']
    export_serializer_class = ExportCeleryLogSerializer

    def clean_all(self, request: Request, *args, **kwargs):
        """
        清空定时任务日志
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.get_queryset().delete()
        return SuccessResponse(msg="清空成功")
