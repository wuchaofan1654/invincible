import request from "@/utils/request";

// 查询缓存详细
export function getApi(query) {
  return request({
    url: "/api/api",
    method: "get",
    params: query
  });
}

// 查询缓存详细
export function getApiDetail(apiId) {
  return request({
    url: "/api/api/" + apiId,
    method: "get",
  });
}

// 查询缓存详细
export function addApi(data) {
  return request({
    url: "/api/api",
    method: "post",
    data: data
  });
}

// 查询缓存详细
export function updateApi(data) {
  return request({
    url: "/api/api",
    method: "post",
    data: data
  });
}

// 查询缓存详细
export function deleteApi(apiId) {
  return request({
    url: "/api/api/" + apiId,
    method: "delete",
  });
}
