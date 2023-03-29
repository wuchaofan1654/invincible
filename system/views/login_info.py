
from rest_framework.request import Request

from framework.filters import DataLevelPermissionsFilter
from framework.response import SuccessResponse
from framework.viewsets import CustomModelViewSet
from system.permissions import CommonPermission
from system.filters import LoginInforFilter
from system.models import LoginInfo
from system.serializers import LoginInforSerializer, ExportLoginInforSerializer


class LoginInfoModelViewSet(CustomModelViewSet):
    """
   登录日志 模型的CRUD视图
   """
    queryset = LoginInfo.objects.all()
    serializer_class = LoginInforSerializer
    filter_class = LoginInforFilter
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    ordering = '-create_datetime'  # 默认排序
    export_field_data = ['访问编号', '用户名称', '登录地址', '登录地点', '浏览器', '操作系统',
                         '登录状态', '操作信息', '登录日期']
    export_serializer_class = ExportLoginInforSerializer

    def clean_all(self, request: Request, *args, **kwargs):
        """
        清空登录日志
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.get_queryset().delete()
        return SuccessResponse(msg="清空成功")

