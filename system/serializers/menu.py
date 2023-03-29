from framework.serializers import CustomModelSerializer
from system.models import Menu
from rest_framework import serializers


# ================================================= #
# ************** 菜单管理 序列化器  ************** #
# ================================================= #

class MenuSerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    parentId = serializers.IntegerField(source="parentId.id", default=0)

    class Meta:
        model = Menu
        exclude = ('description', 'creator', 'modifier')


class MenuCreateUpdateSerializer(CustomModelSerializer):
    """
    菜单管理 创建/更新时的列化器
    """

    def validate(self, attrs: dict):
        # name = attrs['name']
        # role: Role = Role.objects.filter(name=name).first()
        # if role and attrs.get('instanceId', '') != role.instanceId:
        #     raise APIException(message=f'角色名称[{name}]不能重复')
        # if getattr(self.instance, 'is_public', False) or attrs.get('is_public', False):
        #     up = UserPermission(self.request.user)
        #     if not up.is_manager():
        #         raise APIException(message=f'仅Manger能创建/更新角色为公共角色')
        return super().validate(attrs)

    def save(self, **kwargs):
        Menu.delete_cache()
        return super().save(**kwargs)

    class Meta:
        model = Menu
        fields = '__all__'


class MenuTreeSerializer(serializers.ModelSerializer):
    """
    菜单树形架构序列化器:递归序列化所有深度的子菜单
    """
    label = serializers.CharField(source='name', default='')
    parentId = serializers.IntegerField(source="parentId.id", default=0)

    class Meta:
        model = Menu
        fields = ('id', 'label', 'orderNum', 'parentId')

