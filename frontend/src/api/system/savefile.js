import request from "@/utils/request";

// 查询文件列表
export function listSaveFile(query) {
  return request({
    url: "/system/save_file/",
    method: "get",
    params: query
  });
}

// 新增文件
export function addSaveFile(data) {
  return request({
    url: "/system/save_file/",
    method: "post",
    data: data
  });
}

// 删除文件
export function delSaveFile(menuId) {
  return request({
    url: "/system/save_file/" + menuId + "/",
    method: "delete"
  });
}

// 清理废弃文件
export function clearSaveFile() {
  return request({
    url: "/system/clear/save_file/",
    method: "post"
  });
}
