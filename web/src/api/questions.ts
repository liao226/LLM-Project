import {post, get} from '/@/utils/http/axios';

enum URL {
    // 题目和用户答案获取
    getSelect = '/myapp/admin/questions/getSelect',
    getMutiSelect = '/myapp/admin/questions/getMutiSelect',
    getJudge = '/myapp/admin/questions/getJudge',
    getMutiJudge = '/myapp/admin/questions/getMutiJudge',
    getFill = '/myapp/admin/questions/getFill',
    getMutiFill = '/myapp/admin/questions/getMutiFill',
    getCalculate = '/myapp/admin/questions/getCalculate',
    getMutiCalculate = '/myapp/admin/questions/getMutiCalculate',
    getEssay = '/myapp/admin/questions/getEssay',
    getMutiEssay = '/myapp/admin/questions/getMutiEssay',
    // 用户答案更新
    updateSelectAnswer = '/myapp/admin/questions/updateSelectAnswer',
    updateJudgeAnswer = '/myapp/admin/questions/updateJudgeAnswer',
    updateFillAnswer = '/myapp/admin/questions/updateFillAnswer',
    updateCalculateAnswer = '/myapp/admin/questions/updateCalculateAnswer',
    updateEssayAnswer = '/myapp/admin/questions/updateEssayAnswer',
    // 用户答案和flag清空
    clearUserAnswer = '/myapp/admin/questions/clearUserAnswer',
    // 删除错题
    deleteMistakeQuestion = '/myapp/admin/questions/deleteMistakeQuestion'
}

const getSelectApi = async (params: any) => get<any>({
    url: URL.getSelect,
    params: params,
    data: {},
    headers: {}
});

const getMutiSelectApi = async (params: any) => get<any>({
    url: URL.getMutiSelect,
    params: params,
    data: {},
    headers: {}
});

const getJudgeApi = async (params: any) => get<any>({
    url: URL.getJudge,
    params: params,
    data: {},
    headers: {}
});

const getMutiJudgeApi = async (params: any) => get<any>({
    url: URL.getMutiJudge,
    params: params,
    data: {},
    headers: {}
});

const getFillApi = async (params: any) => get<any>({
    url: URL.getFill,
    params: params,
    data: {},
    headers: {}
});

const getMutiFillApi = async (params: any) => get<any>({
    url: URL.getMutiFill,
    params: params,
    data: {},
    headers: {}
});

const getCalculateApi = async (params: any) => get<any>({
    url: URL.getCalculate,
    params: params,
    data: {},
    headers: {}
});

const getMutiCalculateApi = async (params: any) => get<any>({
    url: URL.getMutiCalculate,
    params: params,
    data: {},
    headers: {}
});

const getEssayApi = async (params: any) => get<any>({
    url: URL.getEssay,
    params: params,
    data: {},
    headers: {}
});

const getMutiEssayApi = async (params: any) => get<any>({
    url: URL.getMutiEssay,
    params: params,
    data: {},
    headers: {}
});

const updateSelectAnswerApi = async (data: any) => post<any>({
    url: URL.updateSelectAnswer,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});
const updateJudgeAnswerApi = async (data: any) => post<any>({
    url: URL.updateJudgeAnswer,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});
const updateFillAnswerApi = async (data: any) => post<any>({
    url: URL.updateFillAnswer,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});
const updateCalculateAnswerApi = async (data: any) => post<any>({
    url: URL.updateCalculateAnswer,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});
const updateEssayAnswerApi = async (data: any) => post<any>({
    url: URL.updateEssayAnswer,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const clearUserAnswerApi = async (data: any) => post<any>({
    url: URL.clearUserAnswer,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const deleteMistakeQuestionApi = async (data: any) => post<any>({
    url: URL.deleteMistakeQuestion,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

export {
    getSelectApi,
    getJudgeApi,
    getFillApi,
    getCalculateApi,
    getEssayApi,
    getMutiSelectApi,
    getMutiJudgeApi,
    getMutiFillApi,
    getMutiCalculateApi,
    getMutiEssayApi,
    updateSelectAnswerApi,
    updateJudgeAnswerApi,
    updateFillAnswerApi,
    updateCalculateAnswerApi,
    updateEssayAnswerApi,
    clearUserAnswerApi,
    deleteMistakeQuestionApi,
}