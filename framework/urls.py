# -*- coding: utf-8 -*-
"""
Create by sandy at 20:32 25/03/2022
Description: ToDo
"""
from captcha.conf import settings as ca_settings
from captcha.helpers import captcha_image_url, captcha_audio_url
from captcha.models import CaptchaStore
from django.urls import re_path as url
from django.urls import re_path, include
from rest_framework.views import APIView

from system.views.user import GetUserProfileView, GetRouters
from framework.response import SuccessResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from utils.login import LoginView, LogoutView


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


class CaptchaRefresh(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        new_key = CaptchaStore.pick()
        to_json_response = {
            "key": new_key,
            "image_url": captcha_image_url(new_key),
            "audio_url": captcha_audio_url(new_key) if ca_settings.CAPTCHA_FLITE_PATH else None,
        }
        return SuccessResponse(to_json_response)


urlpatterns = [
    re_path('api-token-auth/', LoginView.as_view(), name='api_token_auth'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'^login/$', LoginView.as_view()),
    re_path(r'^logout/$', LogoutView.as_view()),
    re_path(r'^getInfo/$', GetUserProfileView.as_view()),
    re_path(r'^getRouters/$', GetRouters.as_view()),
    url(r"captcha/refresh/$", CaptchaRefresh.as_view(), name="captcha-refresh"),  # 刷新验证码
    re_path('captcha/', include('captcha.urls')),  # 图片验证码 路由

    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^e(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
