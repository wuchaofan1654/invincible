from framework.serializers import CustomModelSerializer
from system.models import Role
from rest_framework import serializers

from system.serializers import MenuSerializer, DeptSerializer


# ================================================= #
# ************** 角色管理 序列化器  ************** #
# ================================================= #

class RoleSerializer(CustomModelSerializer):
    """
    角色管理 简单序列化器
    """

    class Meta:
        model = Role
        exclude = ('description', 'creator', 'modifier')


class ExportRoleSerializer(CustomModelSerializer):
    """
    导出 角色管理 简单序列化器
    """
    dataScope = serializers.SerializerMethodField()

    def get_data_scope(self, obj):
        data_scope = obj.get_dataScope_display()
        return data_scope

    class Meta:
        model = Role
        fields = ('id', 'roleName', 'roleKey', 'roleSort', 'dataScope', 'status', 'creator', 'modifier', 'remark')


class RoleSimpleSerializer(CustomModelSerializer):
    """
    角色管理 极简单序列化器
    """

    class Meta:
        model = Role
        fields = ('id', 'roleName', 'roleKey', 'status')


class RoleCreateUpdateSerializer(CustomModelSerializer):
    """
    角色管理 创建/更新时的列化器
    """
    menu = MenuSerializer(many=True, read_only=True)
    dept = DeptSerializer(many=True, read_only=True)

    def validate(self, attrs: dict):
        return super().validate(attrs)

    def save(self, **kwargs):
        data = super().save(**kwargs)
        data.dept.set(self.initial_data.get('dept'))
        data.menu.set(self.initial_data.get('menu'))
        return data

    class Meta:
        model = Role
        fields = '__all__'
