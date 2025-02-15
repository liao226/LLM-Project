import {post, get} from '/@/utils/http/axios';

enum URL {
    getSetting = '/myapp/admin/setting/getSetting',  // 获取题型设置信息
    getProgress = '/myapp/admin/setting/getProgress',  // 获取学习进度
    updateFlag = '/myapp/admin/setting/updateFlag',      // 更新题型选择
    updateQuantity = '/myapp/admin/setting/updateQuantity',  // 更新各题型数量设置
    updateProgress = '/myapp/admin/setting/updateProgress',  // 更新学习进度
    updateNextProgress = '/myapp/admin/setting/updateNextProgress',  // 进入下一学习阶段
    updateSelectedGrade = '/myapp/admin/setting/updateSelectedGrade',
    resetSetting = '/myapp/admin/setting/resetSetting',
}

// 获取题型选择结果
const getSettingApi = async (params: any) => get<any>({
    url: URL.getSetting,
    params: params,
    data: {},
    headers: {}
});

// 获取学习进度
const getProgressApi = async (params: any) => get<any>({
    url: URL.getProgress,
    params: params,
    data: {},
    headers: {}
});

// 更新题型选择
const updateFlagApi = async (data: any) => post<any>({
    url: URL.updateFlag,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

// 更新各题型数量设置
const updateQuantityApi = async (data: any) => post<any>({
    url: URL.updateQuantity,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

// 更新学习进度
const updateProgressApi = async (data: any) => post<any>({
    url: URL.updateProgress,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

// 进入下一学习阶段
const updateNextProgressApi = async (data: any) => post<any>({
    url: URL.updateNextProgress,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const updateSelectedGradeApi = async (data: any) => post<any>({
    url: URL.updateSelectedGrade,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const resetSettingApi = async (data: any) => post<any>({
    url: URL.resetSetting,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

export {
    getSettingApi,
    getProgressApi,
    updateFlagApi,
    updateQuantityApi,
    updateProgressApi,
    updateNextProgressApi,
    updateSelectedGradeApi,
    resetSettingApi,
}