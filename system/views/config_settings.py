
from django.conf import settings
from django.core.cache import cache
from rest_framework.request import Request

from framework.filters import DataLevelPermissionsFilter
from framework.response import SuccessResponse
from framework.viewsets import CustomModelViewSet
from system.permissions import CommonPermission
from system.filters import ConfigSettingsFilter
from system.models import ConfigSettings
from system.serializers import ConfigSettingsSerializer, ConfigSettingsCreateUpdateSerializer, \
    ExportConfigSettingsSerializer


class ConfigSettingsModelViewSet(CustomModelViewSet):
    """
    参数设置 模型的CRUD视图
    """
    queryset = ConfigSettings.objects.all()
    serializer_class = ConfigSettingsSerializer
    create_serializer_class = ConfigSettingsCreateUpdateSerializer
    update_serializer_class = ConfigSettingsCreateUpdateSerializer
    filter_class = ConfigSettingsFilter
    search_fields = ('configName',)
    ordering = 'id'  # 默认排序
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    export_field_data = ['参数主键', '参数名称', '参数键名', '参数键值', '系统内置', '参数状态', '创建者', '修改者', '备注']
    export_serializer_class = ExportConfigSettingsSerializer

    def get_config_key(self, request: Request, *args, **kwargs):
        """
        根据 参数键名 查询参数数据信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        config_key_dic = cache.get('system_configKey') if getattr(settings, "REDIS_ENABLE", False) else ""
        if not config_key_dic:
            queryset = self.filter_queryset(self.get_queryset())
            config_key_dic = {ele.get('configKey'): ele.get('configValue') for ele in
                              queryset.values('configValue', 'configKey')}
            if getattr(settings, "REDIS_ENABLE", False):
                cache.set('system_configKey', config_key_dic, 84600)
        return SuccessResponse(msg=config_key_dic.get(kwargs.get('pk'), ''))

    def clearCache(self, request: Request, *args, **kwargs):
        """
        清理键值缓存
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if getattr(settings, "REDIS_ENABLE", False):
            cache.delete('system_configKey')
        return SuccessResponse(msg='清理成功！')
