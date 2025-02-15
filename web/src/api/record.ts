import {post, get} from '/@/utils/http/axios';

enum URL {
    // 出题次数获取和更新
    getIndex = '/myapp/admin/record/getIndex',  // 获取出题次数记录
    addIndex = '/myapp/admin/record/addIndex',  // 新增出题记录
    // 出题记录获取
    getRecord = '/myapp/admin/record/getRecord',
    deleteRecord = '/myapp/admin/record/deleteRecord',
}

// 获取出题次数
const getIndexApi = async (params: any) => get<any>({
    url: URL.getIndex,
    params: params,
    data: {},
    headers: {}
});

// 更新出题次数
const addIndexApi = async (data: any) => post<any>({
    url: URL.addIndex,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const getRecordApi = async (params: any) => get<any>({
    url: URL.getRecord,
    params: params,
    data: {},
    headers: {}
});

// 更新出题次数
const deleteRecordApi = async (data: any) => post<any>({
    url: URL.deleteRecord,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});


export {
    getIndexApi,
    addIndexApi,
    getRecordApi,
    deleteRecordApi,
}