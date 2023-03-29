import django_filters
from system.models import MessagePush


class MessagePushFilter(django_filters.rest_framework.FilterSet):
    """
    消息通知 简单过滤器
    """

    # is_read = django_filters.CharFilter(field_name='messagepushuser_message_push__is_read')
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = MessagePush
        fields = '__all__'