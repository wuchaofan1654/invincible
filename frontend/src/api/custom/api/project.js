import request from "@/utils/request";

// 查询缓存详细
export function getProject(query) {
  return request({
    url: "/api/project",
    method: "get",
    params: query
  });
}

// 查询缓存详细
export function addProject(data) {
  return request({
    url: "/api/project",
    method: "post",
    data: data
  });
}


// 查询缓存详细
export function updateProject(data) {
  return request({
    url: "/api/project",
    method: "post",
    data: data
  });
}

// 查询缓存详细
export function deleteProject(projectId) {
  return request({
    url: "/api/project/" + projectId,
    method: "delete",
  });
}
