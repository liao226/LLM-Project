import {post, get} from '/@/utils/http/axios';

enum URL {
    // 更新用户得分
    updateSelectComment = '/myapp/admin/correct/updateSelectComment',
    updateJudgeComment = '/myapp/admin/correct/updateJudgeComment',
    updateFillComment = '/myapp/admin/correct/updateFillComment',
    updateCalculateComment = '/myapp/admin/correct/updateCalculateComment',
    updateEssayComment = '/myapp/admin/correct/updateEssayComment',
    updateTotalScore = '/myapp/admin/correct/updateTotalScore',
    updateUserScore = '/myapp/admin/correct/updateUserScore',
    getUserScore = '/myapp/admin/correct/getUserScore',
}


const updateSelectCommentApi = async (data: any) => post<any>({
    url: URL.updateSelectComment,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const updateJudgeCommentApi = async (data: any) => post<any>({
    url: URL.updateJudgeComment,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const updateFillCommentApi = async (data: any) => post<any>({
    url: URL.updateFillComment,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const updateCalculateCommentApi = async (data: any) => post<any>({
    url: URL.updateCalculateComment,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const updateEssayCommentApi = async (data: any) => post<any>({
    url: URL.updateEssayComment,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const updateTotalScoreApi = async (data: any) => post<any>({
    url: URL.updateTotalScore,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const updateUserScoreApi = async (data: any) => post<any>({
    url: URL.updateUserScore,
    params: {},
    data: data,
    headers: {'Content-Type': 'multipart/form-data;charset=utf-8'}
});

const getUserScoreApi = async (params: any) => get<any>({
    url: URL.getUserScore,
    params: params,
    data: {},
    headers: {}
});

export {
    updateSelectCommentApi,
    updateJudgeCommentApi,
    updateFillCommentApi,
    updateCalculateCommentApi,
    updateEssayCommentApi,
    updateTotalScoreApi,
    updateUserScoreApi,
    getUserScoreApi,
}