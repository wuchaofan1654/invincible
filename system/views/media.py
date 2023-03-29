from django.contrib.auth import authenticate, get_user_model
from rest_framework.request import Request
from rest_framework.views import APIView

from framework.response import SuccessResponse, ErrorResponse
from system.permissions import CommonPermission, DeptDestroyPermission
from framework.filters import DataLevelPermissionsFilter
from framework.viewsets import CustomModelViewSet
from system.filters import MenuFilter, DeptFilter, PostFilter, RoleFilter, UserProfileFilter, ModuleFilter
from system.models import Role, Menu
from system.serializers import UserProfileSerializer, MenuSerializer, RoleSerializer, \
    MenuCreateUpdateSerializer, DeptSerializer, DeptCreateUpdateSerializer, PostSerializer, PostCreateUpdateSerializer, \
    RoleCreateUpdateSerializer, DeptTreeSerializer, MenuTreeSerializer, UserProfileCreateUpdateSerializer, \
    PostSimpleSerializer, RoleSimpleSerializer, ExportUserProfileSerializer, ExportRoleSerializer, ExportPostSerializer, \
    UserProfileImportSerializer, ModuleSerializer, ModuleTreeSerializer, ModuleCreateUpdateSerializer
from system.models import DictDetails