import request from "@/utils/request";

// 查询获取执行结果
export function getExecuteResult(data) {
  return request({
    url: "/shortcut/result",
    method: "post",
    data: data
  });
}
