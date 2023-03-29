from rest_framework.views import APIView
from framework.response import SuccessResponse
from utils.system_info_utils import get_memory_used_percent, get_cpu_used_percent, get_disk_used_percent


class SystemInfoApiView(APIView):
    """
    系统服务监控视图
    """

    def get(self, request, *args, **kwargs):
        # 获取内存使用率
        memory_used_percent = get_memory_used_percent()
        # 获取cpu使用率
        cpu_used_percent = get_cpu_used_percent()
        # 获取硬盘使用率
        disk_used_percent = get_disk_used_percent()
        return SuccessResponse(
            data={
                "memory_used_percent": memory_used_percent,
                "cpu_used_percent": cpu_used_percent,
                "disk_used_percent": disk_used_percent
            }
        )
