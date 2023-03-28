# -*- coding: utf-8 -*-

from collections import OrderedDict
import json as json_parser
import json

from html import escape as html_escape

text = str
text_types = (str,)


class Json2Html:
    def __init__(self, clubbing=True, escape=True):
        self.table_init_markup = f"<table class='pure-table'>"
        self.clubbing = clubbing
        self.escape = escape

    def convert(self, content="", encode=False):
        if not content:
            json_input = {}
        elif type(content) in text_types:
            try:
                json_input = json_parser.loads(content, object_pairs_hook=OrderedDict)
            except ValueError as e:
                if u"Expecting property name" in text(e):
                    raise e
                json_input = content
        else:
            json_input = content
        converted = self.convert_json_node(json_input)
        if encode:
            return converted.encode('ascii', 'xmlcharrefreplace')
        return converted

    @staticmethod
    def column_headers_from_list_of_dicts(json_input):
        if not json_input \
                or not hasattr(json_input, '__getitem__') \
                or not hasattr(json_input[0], 'keys'):
            return None
        column_headers = json_input[0].keys()
        for entry in json_input:
            if not hasattr(entry, 'keys') \
                    or not hasattr(entry, '__iter__') \
                    or len(entry.keys()) != len(column_headers):
                return None
            for header in column_headers:
                if header not in entry:
                    return None
        return column_headers

    def convert_json_node(self, json_input):
        if type(json_input) in text_types:
            try:
                json_input = json.loads(json_input)
            except:
                return self.escape and html_escape(text(json_input)) or text(json_input)

        if hasattr(json_input, 'items'):
            return self.convert_object(json_input)
        if hasattr(json_input, '__iter__') and hasattr(json_input, '__getitem__'):
            return self.convert_list(json_input)

        return text(json_input)

    def convert_list(self, list_input):
        if not list_input:
            return ""
        converted_output = ""
        column_headers = None
        if self.clubbing:
            column_headers = self.column_headers_from_list_of_dicts(list_input)

        if column_headers is not None:
            converted_output += self.table_init_markup
            converted_output += f'<thead>'
            converted_output += f'<tr><th>' + f'</th><th>'.join(column_headers) + f'</th></tr>'
            converted_output += f'</thead>'
            converted_output += f'<tbody>'
            for list_entry in list_input:
                converted_output += f'<tr><td>'
                converted_output += f'</td><td>'.join(
                    [self.convert_json_node(list_entry[column_header]) for column_header in
                     column_headers])
                converted_output += f'</td></tr>'
            converted_output += f'</tbody>'
            converted_output += f'</table>'
            return converted_output

        converted_output = f'<ul><li>'
        converted_output += f'</li><li>'.join([self.convert_json_node(child) for child in list_input])
        converted_output += f'</li></ul>'
        return converted_output

    def convert_object(self, json_input):
        if not json_input:
            return ""
        converted_output = self.table_init_markup + f"<tr>"
        converted_output += f"</tr><tr>".join([
            f"<th>%s</th><td>%s</td>" % (
                self.convert_json_node(k),
                self.convert_json_node(v)
            )
            for k, v in json_input.items()
        ])
        converted_output += f'</tr></table>'
        return converted_output


if __name__ == '__main__':
    _content = {
        "code": 200,
        "data": {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "interval_list": {
                        "id": 1,
                        "every": 5,
                        "period": "seconds"
                    },
                    "crontab_list": {},
                    "name": "定时获取系统监控信息",
                    "task": "apps.monitor.tasks.get_monitor_info",
                    "args": '[{"monitor_id": 1, "name": "监控数据变化"}, {"monitor_id": 2, "name": "监控数据变化"}]',
                    "kwargs": "{}",
                    "queue": None,
                    "exchange": None,
                    "routing_key": None,
                    "headers": "{}",
                    "priority": None,
                    "expires": None,
                    "expire_seconds": None,
                    "one_off": False,
                    "start_time": None,
                    "enabled": False,
                    "last_run_at": None,
                    "total_run_count": 0,
                    "date_changed": "2022-03-28T15:50:47.034558+08:00",
                    "description": "",
                    "interval": 1,
                    "crontab": None,
                    "solar": None,
                    "clocked": None
                }
            ]
        },
        "msg": "success",
        "status": "success"
    }
    json2html = Json2Html().convert(_content)
    print(json2html)
