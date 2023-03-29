from framework.serializers import CustomModelSerializer
from system.models import Module
from rest_framework import serializers


# ================================================= #
# ************** 模块管理 序列化器  ************** #
# ================================================= #
class ModuleSerializer(CustomModelSerializer):
    """
    模块管理 简单序列化器
    """
    parentId = serializers.IntegerField(source="parentId.id", default=0)

    class Meta:
        model = Module
        fields = '__all__'


class ModuleCreateUpdateSerializer(CustomModelSerializer):
    """
    模块管理 创建/更新时的列化器
    """

    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Module
        fields = '__all__'


class ModuleTreeSerializer(serializers.ModelSerializer):
    """
    模块树形架构序列化器:递归序列化所有深度的子部门
    """
    label = serializers.CharField(source='moduleName', default='')
    parentId = serializers.IntegerField(source="parentId.id", default=0)

    class Meta:
        model = Module
        fields = ('id', 'label', 'parentId', 'status')
