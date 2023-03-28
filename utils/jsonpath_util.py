import logging
from collections.abc import Iterable

import jsonpath


logger = logging.getLogger(__name__)


def get_jsonpath(params: dict = None, exclude_params: list = None, type_params: dict = None):
    if params is None:
        params = {}
    if exclude_params is None:
        exclude_params = []
    _filters = []
    for param_name, param_value in params.items():
        if param_name in exclude_params:
            continue
        if type_params is None or type_params.get(param_name, 'str') == 'str':
            _filter = f"@.{param_name}=='{param_value}'"
        else:
            _filter = f"@.{param_name}=={param_value}"
        _filters.append(_filter)
    _path = " || ".join(_filters)
    if not _path:
        return ""
    return f"[?({_path})]"


def filter_json(obj: list, expr: str, *args, **kwargs):
    if not isinstance(obj, Iterable):
        return []
    if not expr.startswith('$'):
        expr = f"${expr}"
    logger.debug(f"expr={expr}, len={len(obj)}")
    return jsonpath.jsonpath(obj, expr, *args)


def search_json(obj: list, search: str, search_fields: list):
    queryset = []
    search = search.lower()
    for ele in obj:
        for field_name in search_fields:
            value = ele.get(field_name, None)
            if value and search in str(value).lower():
                queryset.append(ele)
                break
    return queryset


class CompareSchema(object):
    def __init__(self):
        self.curr_key = '根节点'
        self.result = {"errors": [], "warnings": []}

    def _non_iterative_diff(self, e, a):
        if not isinstance(a, type(e)):
            self.result["errors"].append(f'{self.curr_key} 字段格式不对: e: {type(e)}; a: {type(a)}')

    def _dict_diff(self, e, a):
        redundancy_keys = [key for key in a.keys() if key not in e.keys()]

        if redundancy_keys:
            self.result["warnings"].append(f'{self.curr_key} 中 字段\"{", ".join(redundancy_keys)}\" 冗余')

        for k, v in e.items():
            self.curr_key = k
            if k not in a.keys():
                self.result["errors"].append(f'{k}字段缺失')
                continue

            self.diff(v, a[k])

    def _list_diff(self, e, a):
        if len(e) > 0:
            e = e[0]

        elif len(e) == 0:
            self.result["warnings"].append(f'e {self.curr_key} 为空数组')
            return

        if len(a) > 0:
            a = a[0]

        elif len(a) == 0:
            self.result["warnings"].append(f'a {self.curr_key} 为空数组')
            return

        self.diff(e, a)

    def diff(self, e, a):
        if not e:
            # self.result["warnings"].append("新埋点第一次录入～")
            return self

        if isinstance(e, list):
            self._list_diff(e, a)

        elif isinstance(e, dict):
            self._dict_diff(e, a)

        else:
            self._non_iterative_diff(e, a)

        return self


if __name__ == '__main__':
    ex = [{
        "name": "sandy",
        "sex": "male",
        "age": 31,
        "hobbits": []
    }]

    au = [{
        "name": "andy",
        "sex": "female",
        "age": "30",
        "age2": "30",
        "age3": "30",
        "age4": "30",
        "hobbits": []
    }]
    print(CompareSchema().diff(ex, au).result)

