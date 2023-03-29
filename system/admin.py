from django.contrib import admin

# Register your models here.

from system.models import Menu, Dept, Role, Post, Module, DictData, DictDetails, ConfigSettings, LoginInfo, \
    OperationLog, CeleryLog, MessagePush, MessagePushUser, SaveFile


admin.site.register(Menu)
admin.site.register(Dept)
admin.site.register(Role)
admin.site.register(Post)
admin.site.register(Module)
admin.site.register(DictData)
admin.site.register(DictDetails)
admin.site.register(ConfigSettings)
admin.site.register(LoginInfo)
admin.site.register(OperationLog)
admin.site.register(CeleryLog)
admin.site.register(MessagePush)
admin.site.register(SaveFile)
