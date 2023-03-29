import request from "@/utils/request";

// 查询菜单列表
export function listMenu(query) {
  return request({
    url: "/system/menus/",
    method: "get",
    params: query
  });
}

// 查询菜单详细
export function getMenu(menuId) {
  return request({
    url: "/system/menus/" + menuId,
    method: "get"
  });
}

// 查询菜单下拉树结构
export function treeselect() {
  return request({
    url: "/system/menus/treeselect/?status=1",
    method: "get"
  });
}

// 根据角色ID查询菜单下拉树结构
export function roleMenuTreeselect(roleId) {
  return request({
    url: "/system/menus/roleMenuTreeselect/" + roleId + "/?status=1",
    method: "get"
  });
}

// 新增菜单
export function addMenu(data) {
  return request({
    url: "/system/menus/",
    method: "post",
    data: data
  });
}

// 修改菜单
export function updateMenu(data) {
  return request({
    url: "/system/menus/" + data.id + "/",
    method: "put",
    data: data
  });
}

// 删除菜单
export function delMenu(menuId) {
  return request({
    url: "/system/menus/" + menuId + "/",
    method: "delete"
  });
}
