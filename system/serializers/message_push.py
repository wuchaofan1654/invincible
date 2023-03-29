from framework.serializers import CustomModelSerializer
from system.models import MessagePush, MessagePushUser
from rest_framework import serializers


# ================================================= #
# ************** 消息通知 序列化器  ************** #
# ================================================= #
class MessagePushSerializer(CustomModelSerializer):
    """
    消息通知 简单序列化器
    """

    class Meta:
        model = MessagePush
        fields = "__all__"

    def save(self, **kwargs):
        return super().save(**kwargs)


class MessagePushCreateUpdateSerializer(CustomModelSerializer):
    """
    消息通知 创建/更新时的列化器
    """

    class Meta:
        model = MessagePush
        fields = "__all__"


class ExportMessagePushSerializer(CustomModelSerializer):
    """
    导出 消息通知 简单序列化器
    """
    users = serializers.CharField(read_only=True)

    def get_users(self, obj):
        return ','.join(MessagePush.objects.filter(id=obj.id).values_list('user__username', flat=True))

    class Meta:
        model = MessagePush
        fields = (
            'id', 'title', 'content', 'message_type', 'is_reviewed', 'status', 'users', 'creator', 'modifier',
            'update_datetime', 'create_datetime')


class MessagePushUserSerializer(CustomModelSerializer):
    """
    消息通知 用户查询简单序列化器
    """
    # users = UserProfileSerializer(read_only=True)
    # users = serializers.SerializerMethodField(read_only=True)
    is_read = serializers.SerializerMethodField(read_only=True)

    # def get_users(self, obj):
    #     return UserProfileSerializer(obj.user.all(), many=True).data
    # 返回这个消息是否已读
    def get_is_read(self, obj):
        object = MessagePushUser.objects.filter(message_push=obj, user=self.context.get('request').user).first()
        return object.is_read if object else False

    class Meta:
        model = MessagePush
        fields = "__all__"

    def save(self, **kwargs):
        return super().save(**kwargs)
