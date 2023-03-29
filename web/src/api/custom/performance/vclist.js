import request from "@/utils/request";

// 查询查询vclist列表
export function listVc(query) {
    return request({
        url: "/performance/vclist/",
        method: "get",
        params: query
    });
}
// 添加白名单
export function addWhite(data) {
    return request({
        url: "/performance/vclist/addwhite",
        method: "post",
        data: data
    });
}
//删除白名单
export function delWhite(data) {
    return request({
        url: "/performance/vclist/delwhite",
        method: "post",
        data: data
    });
}
export function addPoints(data) {
    return request({
        url: "/performance/vclist/upup",
        method: "post",
        data: data
    });
}

export function addVClist(data) {
    return request({
        url: "/performance/vclist/upload",
        method: "post",
        data: data
    });
}
// 发送飞书报警
export function sendFeishu(data) {
    return request({
        url: "/performance/vclist/sendfeishu",
        method: "post",
        data: data
    });
}