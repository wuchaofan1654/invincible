from framework.serializers import CustomModelSerializer
from system.models import ConfigSettings
from django.core.cache import cache
from application import settings

# ================================================= #
# ************** 参数设置 序列化器  ************** #
# ================================================= #

class ConfigSettingsSerializer(CustomModelSerializer):
    """
    参数设置 简单序列化器
    """

    class Meta:
        model = ConfigSettings
        exclude = ('description', 'creator', 'modifier')


class ExportConfigSettingsSerializer(CustomModelSerializer):
    """
    导出 参数设置 简单序列化器
    """

    class Meta:
        model = ConfigSettings
        fields = (
            'id', 'configName', 'configKey', 'configValue', 'configType', 'status', 'creator', 'modifier', 'remark')


class ConfigSettingsCreateUpdateSerializer(CustomModelSerializer):
    """
    参数设置 创建/更新时的列化器
    """

    def save(self, **kwargs):
        if getattr(settings, "REDIS_ENABLE", False):
            cache.delete('system_configKey')
        return super().save(**kwargs)

    class Meta:
        model = ConfigSettings
        fields = '__all__'

