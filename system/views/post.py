
from system.permissions import CommonPermission
from framework.filters import DataLevelPermissionsFilter
from framework.viewsets import CustomModelViewSet
from system.filters import PostFilter
from system.models import Post
from system.serializers import PostSerializer, PostCreateUpdateSerializer, ExportPostSerializer


class PostModelViewSet(CustomModelViewSet):
    """
    岗位管理 的CRUD视图
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    create_serializer_class = PostCreateUpdateSerializer
    update_serializer_class = PostCreateUpdateSerializer
    filter_class = PostFilter
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('postName',)
    ordering = ['postSort', 'create_datetime']  # 默认排序
    export_field_data = ['岗位序号', '岗位编码', '岗位名称', '岗位排序', '状态', '创建者', '修改者', '备注']
    export_serializer_class = ExportPostSerializer
