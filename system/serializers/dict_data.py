from framework.serializers import CustomModelSerializer
from system.models import DictData


class DictDataSerializer(CustomModelSerializer):
    """
    字典管理 简单序列化器
    """

    class Meta:
        model = DictData
        exclude = ('description', 'creator', 'modifier')


class ExportDictDataSerializer(CustomModelSerializer):
    """
    导出 字典管理 简单序列化器
    """

    class Meta:
        model = DictData
        fields = ('id', 'dictName', 'dictType', 'status', 'creator', 'modifier', 'remark',)


class DictDataCreateUpdateSerializer(CustomModelSerializer):
    """
    字典管理 创建/更新时的列化器
    """

    class Meta:
        model = DictData
        fields = '__all__'
