import os

from django.conf import settings


def get_sql(filename):
    """
    获取文件内所有sql
    :param filename: 例如：os.path.join('permission','system_dept.sql')
    :return:
    """
    abspath = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
    pwd = os.path.join(abspath, 'scripts', filename)
    with open(pwd, 'rb') as fp:
        content = fp.read().decode('utf8')
        if filename == "system/system_userprofile.sql":
            user_name = "_".join(settings.AUTH_USER_MODEL.lower().split("."))
            content = content.replace("system_userprofile", user_name). \
                replace("userprofile", settings.AUTH_USER_MODEL.lower().split(".")[-1])
    return [ele for ele in content.split('\n') if not ele.startswith('--') and ele.strip(' ')]
