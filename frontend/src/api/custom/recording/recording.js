import request from "@/utils/request";

// 查询缓存详细
export function getRecording(query) {
  return request({
    url: "/custom/recording",
    method: "get",
    params: query
  });
}

// 查询缓存详细
export function getRecordingDetail(reCordingId) {
  return request({
    url: "/custom/recording" + reCordingId,
    method: "get"
  });
}

// 查询缓存详细
export function addRecording(data) {
  return request({
    url: "/custom/recording",
    method: "post",
    data: data
  });
}

// 查询缓存详细
export function updateRecording(data) {
  return request({
    url: "/custom/recording",
    method: "post",
    data: data
  });
}

// 查询缓存详细
export function deleteRecording(reCordingId) {
  return request({
    url: "/custom/recording" + reCordingId,
    method: "delete"
  });
}
