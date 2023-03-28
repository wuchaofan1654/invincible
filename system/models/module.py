from django.db.models import CASCADE
from django.db.models import CharField, IntegerField, ForeignKey

from framework.models import BaseModel


class Module(BaseModel):
    moduleName = CharField(max_length=64, verbose_name="模块名称")
    orderNum = IntegerField(verbose_name="显示排序")
    owner = CharField(max_length=32, verbose_name="负责人", null=True, blank=True)
    status = CharField(max_length=8, verbose_name="模块状态", null=True, blank=True)
    parentId = ForeignKey(to='Module', on_delete=CASCADE, default=False, verbose_name="上级模块",
                          db_constraint=False, null=True, blank=True)

    class Meta:
        verbose_name = '模块管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.moduleName}"
