import os

from django.conf import settings
from rest_framework.request import Request

from framework.filters import DataLevelPermissionsFilter
from framework.response import SuccessResponse
from framework.viewsets import CustomModelViewSet
from system.permissions import CommonPermission
from system.filters import SaveFileFilter
from system.models import SaveFile
from system.serializers import SaveFileSerializer, SaveFileCreateUpdateSerializer
from utils.file_util import get_all_files, remove_empty_dir, delete_files


class SaveFileModelViewSet(CustomModelViewSet):
    """
   文件管理 模型的CRUD视图
   """
    queryset = SaveFile.objects.all()
    serializer_class = SaveFileSerializer
    create_serializer_class = SaveFileCreateUpdateSerializer
    update_serializer_class = SaveFileCreateUpdateSerializer
    filter_class = SaveFileFilter
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('configName',)
    ordering = '-create_datetime'  # 默认排序

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        return SuccessResponse(serializer.data, status=201, headers=headers)

    def clear_save_file(self, request: Request, *args, **kwargs):
        """
        清理废弃文件
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 获取废弃文件列表
        file_list = get_all_files(os.path.join(settings.MEDIA_ROOT, 'system'))
        queryset_files = [os.path.join(os.path.join(settings.MEDIA_ROOT) + os.sep, ele) for ele in
                          list(self.get_queryset().values_list('file', flat=True))]
        queryset_files_dir = set(map(lambda absdir: os.path.abspath(absdir), queryset_files))
        delete_list = list(set(file_list) - queryset_files_dir)
        # 进行文件删除操作
        delete_files(delete_list)
        # 递归删除空文件
        remove_empty_dir(os.path.join(settings.MEDIA_ROOT, 'system'))
        return SuccessResponse(msg=f"成功清理废弃文件{len(delete_list)}个")
