import request from "@/utils/request";

// 查询埋点列表
export function listPoint(query) {
    return request({
        url: "/point/point/",
        method: "get",
        params: query
    });
}

// 查询埋点列表
export function getPoint(pk) {
    return request({
        url: "/point/point/" + pk + "/",
        method: "get",
    });
}

// 根据unique_name查询埋点列表
export function getPointByUniqueName(unique_name) {
    return request({
        url: "/point/unique_name/" + unique_name + "/",
        method: "get",
    });
}

// 新增埋点
export function addPoint(data) {
    return request({
        url: "/point/point/",
        method: "post",
        data: data
    });
}

// 修改埋点
export function updatePoint(data) {
    return request({
        url: "/point/point/" + data.id + "/",
        method: "put",
        data: data
    });
}

// 删除埋点
export function deletePoint(pk) {
    return request({
        url: "/point/point/" + pk + '/',
        method: "delete",
    });
}


//上传埋点文件
export function addTestPoint(data) {
    return request({
        url: "/point/upload/",
        method: "post",
        data: data
    });
}