import request from "@/utils/request";

// 查询登录日志列表
export function list(query) {
  return request({
    url: "/system/login_info/",
    method: "get",
    params: query
  });
}

// 删除登录日志
export function delLoginInfo(infoId) {
  return request({
    url: `/system/login_info/${infoId}/`,
    method: "delete"
  });
}

// 清空登录日志
export function cleanLoginInfo() {
  return request({
    url: "/system/login_info/clean",
    method: "delete"
  });
}

// 导出登录日志
export function exportLoginInfo(query) {
  return request({
    url: "/system/login_info/export",
    method: "get",
    params: query
  });
}
