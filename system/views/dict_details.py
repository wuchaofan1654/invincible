
from django.conf import settings
from django.core.cache import cache
from rest_framework.request import Request

from framework.filters import DataLevelPermissionsFilter
from framework.response import SuccessResponse
from framework.viewsets import CustomModelViewSet
from system.permissions import CommonPermission
from system.filters import DictDetailsFilter
from system.models import DictDetails
from system.serializers import DictDetailsSerializer, ExportDictDetailsSerializer, DictDetailsCreateUpdateSerializer
from utils.export_excel import export_excel_save_model


class DictDetailsModelViewSet(CustomModelViewSet):
    """
    字典详情 模型的CRUD视图
    """
    queryset = DictDetails.objects.all()
    serializer_class = DictDetailsSerializer
    create_serializer_class = DictDetailsCreateUpdateSerializer
    update_serializer_class = DictDetailsCreateUpdateSerializer
    filter_class = DictDetailsFilter
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('dictLabel',)
    ordering = 'sort'  # 默认排序

    def dict_details_list(self, request: Request, *args, **kwargs):
        """
        根据字典类型查询字典数据信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        dict_details_dic = cache.get('system_dict_details', {}) if getattr(settings, "REDIS_ENABLE", False) else {}
        if not dict_details_dic:
            queryset = self.filter_queryset(self.get_queryset())
            queryset_dic = queryset.order_by('sort').values('dict_data__dictType', 'dictLabel', 'dictValue',
                                                            'is_default')
            for ele in queryset_dic:
                dictType = ele.pop('dict_data__dictType')
                if dictType in dict_details_dic:
                    dict_details_dic[dictType].append(ele)
                else:
                    dict_details_dic[dictType] = [ele]
            if getattr(settings, "REDIS_ENABLE", False):
                cache.set('system_dict_details', dict_details_dic, 84600)
        return SuccessResponse(dict_details_dic.get(kwargs.get('pk'), []))

    def clearCache(self, request: Request, *args, **kwargs):
        """
        清理键值缓存
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if getattr(settings, "REDIS_ENABLE", False):
            cache.delete('system_dict_details')
        return SuccessResponse(msg='清理成功！')

    def export(self, request: Request, *args, **kwargs):
        """
        导出字典详情数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        dictType = request.query_params.get('dictType')
        field_data = ['字典详情主键', '字典标签', '字典键值', '是否默认', '字典状态', '字典排序', '创建者', '修改者', '备注']
        data = ExportDictDetailsSerializer(DictDetails.objects.filter(dict_data__dictType=dictType), many=True).data
        return SuccessResponse(export_excel_save_model(request, field_data, data, f'导出字典[{dictType}]详情数据.xls'))
