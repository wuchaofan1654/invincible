
from rest_framework.request import Request

from framework.filters import DataLevelPermissionsFilter
from framework.response import SuccessResponse
from framework.viewsets import CustomModelViewSet
from system.permissions import CommonPermission
from system.filters import OperationLogFilter
from system.models import OperationLog
from system.serializers import OperationLogSerializer, ExportOperationLogSerializer


class OperationLogModelViewSet(CustomModelViewSet):
    """
   操作日志 模型的CRUD视图
   """
    queryset = OperationLog.objects.all()
    serializer_class = OperationLogSerializer
    filter_class = OperationLogFilter
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    ordering = '-create_datetime'  # 默认排序
    export_field_data = ['请求模块', '请求地址', '请求参数', '请求方式', '操作说明', '请求ip地址',
                         '请求浏览器', '响应状态码', '操作地点', '操作系统', '返回信息', '响应状态', '操作用户名']
    export_serializer_class = ExportOperationLogSerializer

    def clean_all(self, request: Request, *args, **kwargs):
        """
        清空操作日志
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.get_queryset().delete()
        return SuccessResponse(msg="清空成功")
