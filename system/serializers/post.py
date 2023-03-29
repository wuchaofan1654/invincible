from framework.serializers import CustomModelSerializer
from system.models import Post


# ================================================= #
# ************** 岗位管理 序列化器  ************** #
# ================================================= #

class PostSerializer(CustomModelSerializer):
    """
    岗位管理 简单序列化器
    """

    class Meta:
        model = Post
        exclude = ('description', 'creator', 'modifier')


class ExportPostSerializer(CustomModelSerializer):
    """
    导出 岗位管理 简单序列化器
    """

    class Meta:
        model = Post
        fields = ('id', 'postName', 'postCode', 'postSort', 'status', 'creator', 'modifier', 'remark')


class PostSimpleSerializer(CustomModelSerializer):
    """
    岗位管理 极简单序列化器
    """

    class Meta:
        model = Post
        fields = ('id', 'postName', 'postCode', 'status')


class PostCreateUpdateSerializer(CustomModelSerializer):
    """
    岗位管理 创建/更新时的列化器
    """

    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Post
        fields = '__all__'
