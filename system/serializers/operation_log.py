from framework.serializers import CustomModelSerializer
from system.models import OperationLog


# ================================================= #
# ************** 操作日志 序列化器  ************** #
# ================================================= #

class OperationLogSerializer(CustomModelSerializer):
    """
    操作日志 简单序列化器
    """

    class Meta:
        model = OperationLog
        fields = "__all__"


class ExportOperationLogSerializer(CustomModelSerializer):
    """
    导出 操作日志 简单序列化器
    """

    class Meta:
        model = OperationLog
        fields = ('request_modular', 'request_path', 'request_body', 'request_method', 'request_msg', 'request_ip',
                  'request_browser', 'response_code', 'request_location', 'request_os', 'json_result', 'status',
                  'creator_name')
