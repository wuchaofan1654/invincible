import request from "@/utils/request";

// 查询缓存详细
export function getCheckResult(query) {
  return request({
    url: "/custom/check_result",
    method: "get",
    params: query
  });
}

// 查询缓存详细
export function getCheckResultDetail(checkResultId) {
  return request({
    url: "/custom/check_result" + checkResultId,
    method: "get"
  });
}

// 查询缓存详细
export function addCheckResult(data) {
  return request({
    url: "/custom/check_result",
    method: "post",
    data: data
  });
}

// 查询缓存详细
export function updateCheckResult(data) {
  return request({
    url: "/custom/check_result",
    method: "post",
    data: data
  });
}

// 查询缓存详细
export function deleteCheckResult(checkResultId) {
  return request({
    url: "/custom/check_result" + checkResultId,
    method: "delete"
  });
}
