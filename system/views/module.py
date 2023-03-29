from rest_framework.request import Request

from framework.response import SuccessResponse
from framework.viewsets import CustomModelViewSet
from system.filters import ModuleFilter
from system.models import Module
from system.serializers import ModuleSerializer, ModuleTreeSerializer, ModuleCreateUpdateSerializer


class ModuleModelViewSet(CustomModelViewSet):
    """
    模块管理 的CRUD视图
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    create_serializer_class = ModuleCreateUpdateSerializer
    update_serializer_class = ModuleCreateUpdateSerializer
    filter_class = ModuleFilter
    # extra_filter_backends = [DataLevelPermissionsFilter]
    # update_extra_permission_classes = (CommonPermission,)
    # destroy_extra_permission_classes = (CommonPermission, DestroyPermission)
    # create_extra_permission_classes = (CommonPermission,)
    # search_fields = ('',)
    ordering = 'create_datetime'  # 默认排序

    def tree_select_list(self, request: Request, *args, **kwargs):
        """
        递归获取模块树
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = self.filter_queryset(self.get_queryset())
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        serializer = ModuleTreeSerializer(queryset, many=True)
        return SuccessResponse(serializer.data)
