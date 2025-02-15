import {post} from '/@/utils/http/axios';

enum URL {
    // 题目生成
    generateSelect = '/myapp/admin/generate/generateSelect',  // 选择题
    generateJudge = '/myapp/admin/generate/generateJudge',  // 判断题
    generateFill = '/myapp/admin/generate/generateFill',  // 填空题
    generateCalculate = '/myapp/admin/generate/generateCalculate',  // 计算题
    generateEssay = '/myapp/admin/generate/generateEssay',  // 应用题
}


// 出题
const generateSelectApi = async (data: any) => post<any>({
    url: URL.generateSelect,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});


const generateJudgeApi = async (data: any) => post<any>({
    url: URL.generateJudge,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});


const generateFillApi = async (data: any) => post<any>({
    url: URL.generateFill,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});


const generateCalculateApi = async (data: any) => post<any>({
    url: URL.generateCalculate,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});


const generateEssayApi = async (data: any) => post<any>({
    url: URL.generateEssay,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});


export {
    generateSelectApi,
    generateJudgeApi,
    generateFillApi,
    generateCalculateApi,
    generateEssayApi,
}