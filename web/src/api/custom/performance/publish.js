import request from "@/utils/request";

// 查询埋点列表
export function comparePublish(pk1, pk2) {
    return request({
        url: "/performance/publish/compare/" + pk1 + "/" + pk2 + "/",
        method: "get"
    });
}
// 下载json接口
export function download_json_file(query) {
    return request({
        url: "/performance/publish/downloadjson/",
        method: "get",
        responseType: 'blob',
        params: query
    });
}

// 展示所有发布记录
export function listPublish(query) {
    return request({
        url: "/performance/publish/",
        method: "get",
        params: query
    });
}

// 删除发布记录
export function deletePublish(pk) {
    return request({
        url: "/performance/publish/delete/" + pk + "/",
        method: "post"
    });
}

// 查询版本列表
export function listBuildNo(query) {
    return request({
        url: "/performance/publish/options/build",
        method: "get",
        params: query
    });
}

// 通过json文件添加发布记录数据
export function addPublish(data) {
    return request({
        url: "/performance/publish/",
        method: "post",
        data: data
    });
}

export function get_publish_stat(data) {
    return request({
        url: "/performance/publish/stat/",
        method: "post",
        data: data
    });
}

export function send_alert(data) {
    return request({
        url: "/performance/publish/compareAlert/",
        method: "post",
        data: data
    });
}
// 查询版本号列表
export function getVersionList(query) {
    return request({
        url: "/performance/publish/getVersionList/",
        method: "get",
        params: query
    });
}