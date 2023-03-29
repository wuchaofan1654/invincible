from django.urls import re_path
from rest_framework.routers import DefaultRouter

from system.views.menu import MenuModelViewSet
from system.views.dept import DeptModelViewSet
from system.views.post import PostModelViewSet
from system.views.role import RoleModelViewSet
from system.views.user import UserProfileModelViewSet
from system.views.module import ModuleModelViewSet

from system.views.dict_data import DictDataModelViewSet
from system.views.dict_details import DictDetailsModelViewSet
from system.views.config_settings import ConfigSettingsModelViewSet
from system.views.save_file import SaveFileModelViewSet
from system.views.message_push import MessagePushModelViewSet
from system.views.login_info import LoginInfoModelViewSet
from system.views.operation_log import OperationLogModelViewSet
from system.views.celery_log import CeleryLogModelViewSet
from system.views.system_info import SystemInfoApiView


router = DefaultRouter()
router.register(r'menus', MenuModelViewSet)
router.register(r'dept', DeptModelViewSet)
router.register(r'dept/exclude', DeptModelViewSet)
router.register(r'post', PostModelViewSet)
router.register(r'role', RoleModelViewSet)
router.register(r'user', UserProfileModelViewSet)
router.register(r'module', ModuleModelViewSet)
router.register(r'dict/type', DictDataModelViewSet)
router.register(r'dict/data', DictDetailsModelViewSet)
router.register(r'config', ConfigSettingsModelViewSet)
router.register(r'save_file', SaveFileModelViewSet)
router.register(r'message', MessagePushModelViewSet)
router.register(r'login_info', LoginInfoModelViewSet)
router.register(r'operation_log', OperationLogModelViewSet)
router.register(r'celery_log', CeleryLogModelViewSet)

urlpatterns = [
    re_path('dept/exclude/(?P<pk>.*)/', DeptModelViewSet.as_view({'get': 'exclude_list'})),
    re_path('dept/tree_select/', DeptModelViewSet.as_view({'get': 'tree_select_list'})),
    re_path('menus/tree_select/', MenuModelViewSet.as_view({'get': 'tree_select_list'})),
    # 根据角色ID查询菜单下拉树结构
    re_path('menus/role_menu_tree_select/(?P<pk>.*)/', MenuModelViewSet.as_view({'get': 'role_menu_tree_select'})),
    # 根据角色ID查询部门树结构
    re_path('dept/role_dept_tree_select/(?P<pk>.*)/', DeptModelViewSet.as_view({'get': 'role_dept_tree_select'})),
    # 更新状态
    re_path('user/change_status/', UserProfileModelViewSet.as_view({'put': 'change_status'})),

    re_path('module/tree_select/', ModuleModelViewSet.as_view({'get': 'tree_select_list'})),

    # 获取用户详情
    re_path('user/details/', UserProfileModelViewSet.as_view({'get': 'get_user_details'})),
    # 后台重置密码
    re_path('user/reset_pwd/', UserProfileModelViewSet.as_view({'put': 'reset_pwd'})),
    # 用户自己重置密码
    re_path('user/profile/update_pwd/', UserProfileModelViewSet.as_view({'put': 'update_pwd'})),
    # 更新用户头像
    re_path('user/profile/avatar/', UserProfileModelViewSet.as_view({'put': 'put_avatar'})),
    # 获取、更新用户个人信息
    re_path('user/profile/', UserProfileModelViewSet.as_view({'get': 'profile', 'put': 'put_profile'})),
    # 导出用户
    re_path('user/export/', UserProfileModelViewSet.as_view({'get': 'export', })),
    # 导出角色
    re_path('role/export/', RoleModelViewSet.as_view({'get': 'export', })),
    # 导出岗位
    re_path('post/export/', PostModelViewSet.as_view({'get': 'export', })),
    # 用户导入模板下载及导入
    re_path('user/import_template/',
            UserProfileModelViewSet.as_view({'get': 'import_template', 'post': 'import_template'})),
    re_path('dict/get/type/(?P<pk>.*)/', DictDetailsModelViewSet.as_view({'get': 'dict_details_list'})),
    re_path('config/config_key/(?P<pk>.*)/', ConfigSettingsModelViewSet.as_view({'get': 'get_config_key'})),
    # 参数管理导出
    re_path('config/export/', ConfigSettingsModelViewSet.as_view({'get': 'export'})),
    # 清理参数缓存
    re_path('config/clear_cache/', ConfigSettingsModelViewSet.as_view({'delete': 'clearCache', })),
    # 导出字典管理数据
    re_path('dict/type/export/', DictDataModelViewSet.as_view({'get': 'export'})),
    # 导出字典详情数据
    re_path('dict/data/export/', DictDetailsModelViewSet.as_view({'get': 'export'})),
    # 清理字典缓存
    re_path('dict/type/clear_cache/', DictDetailsModelViewSet.as_view({'delete': 'clearCache', })),
    # 消息通知导出
    re_path('message/export/', MessagePushModelViewSet.as_view({'get': 'export', })),
    # 用户个人消息列表
    re_path('message/user_messages/', MessagePushModelViewSet.as_view({'get': 'get_user_messages', })),
    # 改为已读
    re_path('message/is_read/(?P<pk>.*)/', MessagePushModelViewSet.as_view({'put': 'update_is_read', })),
    # 清空操作日志
    re_path('operation_log/clean/', OperationLogModelViewSet.as_view({'delete': 'clean_all', })),
    # 导出操作日志
    re_path('operation_log/export/', OperationLogModelViewSet.as_view({'get': 'export', })),
    # 清空登录日志
    re_path('login_info/clean/', LoginInfoModelViewSet.as_view({'delete': 'clean_all', })),
    # 导出登录日志
    re_path('login_info/export/', LoginInfoModelViewSet.as_view({'get': 'export', })),
    # 清空定时日志
    re_path('celery_log/clean/', CeleryLogModelViewSet.as_view({'delete': 'clean_all', })),
    # 导出定时日志
    re_path('celery_log/export/', CeleryLogModelViewSet.as_view({'get': 'export', })),
    # 清除废弃文件
    re_path('clear/save_file/', SaveFileModelViewSet.as_view({'post': 'clear_save_file', })),
    # 获取系统信息cpu、内存、硬盘
    re_path('sys/info/', SystemInfoApiView.as_view())

]
urlpatterns += router.urls
