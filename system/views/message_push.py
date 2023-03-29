
from django.db.models import Q
from rest_framework.request import Request

from framework.response import SuccessResponse
from framework.viewsets import CustomModelViewSet
from system.permissions import CommonPermission
from system.filters import MessagePushFilter, MessagePush
from system.models import MessagePushUser
from system.serializers import MessagePushSerializer, MessagePushCreateUpdateSerializer, ExportMessagePushSerializer


class MessagePushModelViewSet(CustomModelViewSet):
    """
    消息推送模型的CRUD视图
    """
    queryset = MessagePush.objects.all()
    serializer_class = MessagePushSerializer
    create_serializer_class = MessagePushCreateUpdateSerializer
    update_serializer_class = MessagePushCreateUpdateSerializer
    # extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    filter_class = MessagePushFilter
    ordering = "-update_datetime"  # 默认排序
    export_field_data = ['消息序号', '标题', '内容', '消息类型', '是否审核', '消息状态', '通知接收消息用户',
                         '创建者', '修改者', '修改时间', '创建时间']
    export_serializer_class = ExportMessagePushSerializer

    def get_user_messages(self, request: Request, *args, **kwargs):
        """
        获取用户自己消息列表
        """
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(status=2)
        is_read = request.query_params.get('is_read', None)
        if is_read:
            if is_read == 'False':
                queryset = queryset.exclude(Q(messagepushuser_message_push__is_read=True),
                                            Q(messagepushuser_message_push__user=request.user))
            elif is_read == 'True':
                queryset = queryset.filter(messagepushuser_message_push__is_read=True,
                                           messagepushuser_message_push__user=request.user)
        queryset = queryset.filter(is_reviewed=True).distinct()
        page = self.paginate_queryset(queryset)
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        if page is not None:
            if getattr(self, 'values_queryset', None):
                return self.get_paginated_response(page)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        if getattr(self, 'values_queryset', None):
            return SuccessResponse(page)
        serializer = self.get_serializer(queryset, many=True)
        return SuccessResponse(serializer.data)

    def update_is_read(self, request: Request, *args, **kwargs):
        """
        修改为已读
        """
        instance, _ = MessagePushUser.objects.get_or_create(message_push_id=kwargs.get('pk'), user=request.user)
        instance.is_read = True
        instance.save()
        return SuccessResponse()

