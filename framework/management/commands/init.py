import logging
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection

from framework.scripts import get_sql

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    项目初始化命令: python manage.py init
    """

    def custom_sql(self, sql_list, model_name, table_name, overwrite_yn):
        """
        批量执行sql
        :param overwrite_yn:
        :param model_name:
        :param sql_list:
        :param table_name: 表名
        :return:
        """
        with connection.cursor() as cursor:
            num = 0
            for ele in table_name.split(','):
                cursor.execute("select count(*) from {}".format(ele))
                result = cursor.fetchone()
                num += result[0]
            if num > 0:
                while True:
                    if overwrite_yn is None:
                        inp = input(f'[{model_name}]模型已初始化完成，继续将清空[{table_name}]表中所有数据，是否继续初始化？【 Y/N 】')
                    else:
                        inp = 'Y' if overwrite_yn else 'N'
                    if inp.upper() == 'N':
                        return False
                    elif inp.upper() == 'Y':
                        logger.info(f'正在清空[{table_name}]中数据...')
                        cursor.execute("SET foreign_key_checks = 0")
                        for ele in table_name.split(','):
                            cursor.execute("truncate table {};".format(ele))
                        cursor.execute("SET foreign_key_checks = 1")
                        connection.commit()
                        logger.info(f'清空[{table_name}]中数据{result[0]}条')
                        break

            for sql in sql_list:
                try:
                    cursor.execute(sql)
                except Exception as e:
                    print(e)
            connection.commit()
            return True

    def init(self, sql_filename, model_name, table_name, overwrite_yn):
        """
        初始化
        :param overwrite_yn:
        :param sql_filename: sql存放位置
        :param model_name: 模块名
        :param table_name: 表名
        :return:
        """
        logger.info(f'正在初始化[{model_name}]中...')
        if self.custom_sql(get_sql(sql_filename), model_name, table_name, overwrite_yn):
            logger.info(f'[{model_name}]初始化完成！')
        else:
            logger.info(f'已取消[{table_name}]初始化')

    def add_arguments(self, parser):
        parser.add_argument('init_name', nargs='*', type=str, )
        parser.add_argument('-y', nargs='*')
        parser.add_argument('-Y', nargs='*')
        parser.add_argument('-n', nargs='*')
        parser.add_argument('-N', nargs='*')

    def handle(self, *args, **options):
        user_name = "_".join(settings.AUTH_USER_MODEL.lower().split("."))
        init_dict = {
            'system_dict_data': [os.path.join('system', 'system_dict_data.sql'), '字典管理', 'system_dictdata'],
            'system_dict_details': [os.path.join('system', 'system_dict_details.sql'), '字典详情', 'system_dictdetails'],
            'system_config_settings': [os.path.join('system', 'system_config_settings.sql'), '参数设置',
                                       'system_configsettings'],
            'system_post': [os.path.join('system', 'system_post.sql'), '岗位管理', 'system_post'],
            'system_dept': [os.path.join('system', 'system_dept.sql'), '部门管理', 'system_dept'],
            'system_menu': [os.path.join('system', 'system_menu.sql'), '菜单管理', 'system_menu'],
            'system_role': [os.path.join('system', 'system_role.sql'), '角色管理',
                            ','.join(['system_role', 'system_role_dept', 'system_role_menu'])],
            'system_userprofile': [os.path.join('system', 'system_userprofile.sql'), '用户管理', ','.join(
                [f'{user_name}_groups', f'{user_name}', f'{user_name}_role', f'{user_name}_post'])]
        }
        init_name = options.get('init_name')
        overwrite_yn = None
        if isinstance(options.get('y'), list) or isinstance(options.get('Y'), list):
            overwrite_yn = True
        if isinstance(options.get('n'), list) or isinstance(options.get('N'), list):
            overwrite_yn = False
        if init_name:
            [self.init(*init_dict[ele], overwrite_yn=overwrite_yn) for ele in init_name if ele in init_dict]
        else:
            for ele in init_dict.values():
                self.init(*ele, overwrite_yn=overwrite_yn)
