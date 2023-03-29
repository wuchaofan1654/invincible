from framework.serializers import CustomModelSerializer
from system.models import DictDetails
from rest_framework import serializers

from django.core.cache import cache
from application import settings


# ================================================= #
# ************** 字典详情 序列化器  ************** #
# ================================================= #

class DictDetailsSerializer(CustomModelSerializer):
    """
    字典详情 简单序列化器
    """
    dictType = serializers.CharField(source='dict_data.dictType', default='', read_only=True)

    class Meta:
        model = DictDetails
        exclude = ('description', 'creator', 'modifier')


class ExportDictDetailsSerializer(CustomModelSerializer):
    """
    导出 字典详情 简单序列化器
    """

    class Meta:
        model = DictDetails
        fields = ('id', 'dictLabel', 'dictValue', 'is_default', 'status', 'sort', 'creator', 'modifier', 'remark',)


class DictDetailsListSerializer(CustomModelSerializer):
    """
    字典详情List 简单序列化器
    """

    class Meta:
        model = DictDetails
        fields = ('dictLabel', 'dictValue', 'is_default')


class DictDetailsCreateUpdateSerializer(CustomModelSerializer):
    """
    字典详情 创建/更新时的列化器
    """

    def save(self, **kwargs):
        if getattr(settings, "REDIS_ENABLE", False):
            cache.delete('system_dict_details')
        return super().save(**kwargs)

    class Meta:
        model = DictDetails
        fields = '__all__'

