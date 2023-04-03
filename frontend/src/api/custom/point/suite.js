import request from "@/utils/request";

// 查询埋点集合列表
export function listSuite(query) {
  return request({
    url: "/point/suite/",
    method: "get",
    params: query
  });
}

// 查询埋点列表
export function getSuite(pk) {
  return request({
    url: "/point/suite/" + pk + "/",
    method: "get",
  });
}

// 新增埋点
export function addSuite(query) {
  return request({
    url: "/point/suite/",
    method: "post",
    params: query
  });
}

// 修改埋点
export function updateSuite(query) {
  return request({
    url: "/point/suite/",
    method: "put",
    params: query
  });
}

// 删除埋点
export function deleteSuite(pk) {
  return request({
    url: "/point/suite/" + pk + '/',
    method: "delete",
  });
}

