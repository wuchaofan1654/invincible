import request from "@/utils/request";

// 查询埋点检查记录列表
export function listIntercept(query) {
  return request({
    url: "/point/intercept/",
    method: "get",
    params: query
  });
}

// 查询埋点列表
export function getIntercept(pk) {
  return request({
    url: "/point/intercept/" + pk + "/",
    method: "get",
  });
}

// 新增埋点
export function addIntercept(query) {
  return request({
    url: "/point/intercept/",
    method: "post",
    params: query
  });
}

// 修改埋点
export function updateIntercept(query) {
  return request({
    url: "/point/intercept/",
    method: "put",
    params: query
  });
}

// 删除埋点
export function deleteIntercept(pk) {
  return request({
    url: "/point/intercept/" + pk + '/',
    method: "delete",
  });
}
