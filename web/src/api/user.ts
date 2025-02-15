import {get, post} from '/@/utils/http/axios';

enum URL {
    login = '/myapp/admin/adminLogin',  // 登录
    add = '/myapp/admin/user/add',      // 用户注册
    updatePwd = '/myapp/admin/user/updatePwd',  // 修改密码
    updateUsername = '/myapp/admin/user/updateUsername',  // 修改用户名
    deleteUser = '/myapp/admin/user/deleteUser',  // 注销账户
    clickAvatar = '/myapp/admin/user/clickAvatar',
}

export interface LoginData {
    username: string;
    password: string;
}

// 用户登录
const loginApi = async (data: LoginData) => post<any>({
    url: URL.login,
    data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

// 新增用户
const addApi = async (data: any) => post<any>({
    url: URL.add,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
})

// 修改用户密码
const updatePwdApi = async (data: any) => post<any>({
    url: URL.updatePwd,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

// 修改账户名
const updateUsernameApi = async (data: any) => post<any>({
    url: URL.updateUsername,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

// 注销账户
const deleteUserApi = async (data: any) => post<any>({
    url: URL.deleteUser,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const clickAvatarApi = async (params: any) => get<any>({
    url: URL.clickAvatar,
    params: params,
    data: {},
    headers: {}
});

export {
    loginApi,
    addApi,
    updatePwdApi,
    updateUsernameApi,
    deleteUserApi,
    clickAvatarApi,
};
