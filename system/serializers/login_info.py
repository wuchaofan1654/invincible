from framework.serializers import CustomModelSerializer
from system.models import LoginInfo


# ================================================= #
# ************** 登录日志 序列化器  ************** #
# ================================================= #

class LoginInforSerializer(CustomModelSerializer):
    """
    登录日志 简单序列化器
    """

    class Meta:
        model = LoginInfo
        fields = "__all__"


class ExportLoginInforSerializer(CustomModelSerializer):
    """
    导出 登录日志 简单序列化器
    """

    class Meta:
        model = LoginInfo
        fields = ('id', 'creator_name', 'ipaddr', 'loginLocation', 'browser', 'os',
                  'status', 'msg')

