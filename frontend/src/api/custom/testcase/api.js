import request from "@/utils/request";

// 查询缓存详细
export function getApi() {
  return request({
    url: "/api/api",
    method: "get"
  });
}
