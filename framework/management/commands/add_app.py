import logging
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection

from application.settings import BASE_DIR
from framework.scripts import get_sql

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    项目初始化命令: python manage.py add_app
    """

    def __init__(self):
        self.custom_dir = os.path.join(BASE_DIR, 'custom')
        super().__init__()

    def create_models(self, app_name):
        pass

    def create_filters(self, app_name):
        pass

    def create_serializers(self, app_name):
        pass

    def create_views(self, app_name):
        pass

    def add_arguments(self, parser):
        parser.add_argument('app_name', nargs='*', type=str, )

    def handle(self, *args, **options):
        app_name = options.get('app_name')
        self.create_models(app_name)
