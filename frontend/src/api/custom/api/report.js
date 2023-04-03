import request from "@/utils/request";

// 查询缓存详细
export function getReport(query) {
  return request({
    url: "/api/report",
    method: "get",
    params: query
  });
}

// 查询缓存详细
export function addReport(data) {
  return request({
    url: "/api/report",
    method: "post",
    data: data
  });
}


// 查询缓存详细
export function updateReport(data) {
  return request({
    url: "/api/report",
    method: "post",
    data: data
  });
}

// 查询缓存详细
export function deleteReport(reportId) {
  return request({
    url: "/api/report/" + reportId,
    method: "delete",
  });
}
