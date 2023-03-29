from framework.serializers import CustomModelSerializer
from system.models import SaveFile
from rest_framework import serializers


# ================================================= #
# ************** 文件管理 序列化器  ************** #
# ================================================= #

class SaveFileSerializer(CustomModelSerializer):
    """
    文件管理 简单序列化器
    """
    file_url = serializers.CharField(source='file.url', read_only=True)

    class Meta:
        model = SaveFile
        exclude = ('description',)


class SaveFileCreateUpdateSerializer(CustomModelSerializer):
    """
    文件管理 创建/更新时的列化器
    """
    file_url = serializers.SerializerMethodField(read_only=True)

    def get_file_url(self, obj: SaveFile):
        return getattr(obj.file, "url", obj.file) if hasattr(obj, "file") else ""

    def save(self, **kwargs):
        files = self.context.get('request').FILES.get('file')
        self.validated_data['name'] = files.name
        self.validated_data['size'] = files.size
        self.validated_data['type'] = files.content_type
        self.validated_data['address'] = '本地存储'
        self.validated_data['source'] = '用户上传'
        instance = super().save(**kwargs)
        # 进行判断是否需要OSS上传
        return instance

    class Meta:
        model = SaveFile
        fields = '__all__'
