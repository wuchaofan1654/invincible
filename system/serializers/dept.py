from framework.serializers import CustomModelSerializer
from system.models import Dept
from rest_framework import serializers


# ================================================= #
# ************** 部门管理 序列化器  ************** #
# ================================================= #

class DeptSerializer(CustomModelSerializer):
    """
    部门管理 简单序列化器
    """
    parentId = serializers.IntegerField(source="parentId.id", default=0)

    class Meta:
        model = Dept
        exclude = ('description', 'creator', 'modifier')


class DeptCreateUpdateSerializer(CustomModelSerializer):
    """
    部门管理 创建/更新时的列化器
    """

    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Dept
        fields = '__all__'


class DeptTreeSerializer(serializers.ModelSerializer):
    """
    部门树形架构序列化器:递归序列化所有深度的子部门
    """
    label = serializers.CharField(source='deptName', default='')
    parentId = serializers.IntegerField(source="parentId.id", default=0)

    class Meta:
        model = Dept
        fields = ('id', 'label', 'parentId', 'status')

