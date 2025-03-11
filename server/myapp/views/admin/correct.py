# Create your views here.

from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import GenerateRecord, SelectQuestion, JudgeQuestion, FillQuestion, CalculateQuestion, \
    EssayQuestion
from myapp.serializers import GenerateRecordSerializer

from myapp.utils import get_question_comment, get_score, get_record_comment


# 更新用户各题型得分和试卷总分
@api_view(['POST'])
def update_select_comment(request):
    questions = SelectQuestion.objects.filter(username=request.data['username'], index=request.data['index']).order_by(
        'id')
    question = questions[int(request.data['question_idx'])]

    data = get_question_comment(question.question, question.solution, question.user_answer, question.comment)
    # 更新题目评论
    question.flag = data['flag']
    # question.comment = data['comment']
    question.save()

    return APIResponse(code=0, message='解析更新成功')


@api_view(['POST'])
def update_judge_comment(request):
    questions = JudgeQuestion.objects.filter(username=request.data['username'], index=request.data['index']).order_by(
        'id')
    question = questions[int(request.data['question_idx'])]

    data = get_question_comment(question.question, question.solution, question.user_answer, question.comment)
    # 更新题目评论
    question.flag = data['flag']
    # question.comment = data['comment']
    question.save()

    return APIResponse(code=0, message='解析更新成功')


@api_view(['POST'])
def update_fill_comment(request):
    questions = FillQuestion.objects.filter(username=request.data['username'], index=request.data['index']).order_by(
        'id')
    question = questions[int(request.data['question_idx'])]

    data = get_question_comment(question.question, question.solution, question.user_answer, question.comment)
    # 更新题目评论
    question.flag = data['flag']
    # question.comment = data['comment']
    question.save()

    return APIResponse(code=0, message='解析更新成功')


@api_view(['POST'])
def update_calculate_comment(request):
    questions = CalculateQuestion.objects.filter(username=request.data['username'],
                                                 index=request.data['index']).order_by(
        'id')
    question = questions[int(request.data['question_idx'])]

    data = get_question_comment(question.question, question.solution, question.user_answer, question.comment)
    # 更新题目评论
    question.flag = data['flag']
    # question.comment = data['comment']
    question.save()

    return APIResponse(code=0, message='解析更新成功')


@api_view(['POST'])
def update_essay_comment(request):
    questions = EssayQuestion.objects.filter(username=request.data['username'], index=request.data['index']).order_by(
        'id')
    question = questions[int(request.data['question_idx'])]

    data = get_question_comment(question.question, question.solution, question.user_answer, question.comment)
    # 更新题目评论
    question.flag = data['flag']
    # question.comment = data['comment']
    question.save()

    return APIResponse(code=0, message='解析更新成功')


@api_view(['POST'])
def update_total_score(request):
    record = GenerateRecord.objects.get(username=request.data['username'], index=request.data['index'])
    record.total_score = 0

    # 统计分数并更新数据库
    select_questions = SelectQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    judge_questions = JudgeQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    fill_questions = FillQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    calculate_questions = CalculateQuestion.objects.filter(username=request.data['username'],
                                                           index=request.data['index'])
    essay_questions = EssayQuestion.objects.filter(username=request.data['username'], index=request.data['index'])

    record.total_score = (len(select_questions) + len(judge_questions) + len(fill_questions) + len(
        calculate_questions)) * 2 + len(essay_questions) * 6

    record.save()

    return APIResponse(code=0, message='更新结束')


# 更新用户得分，并获取新的评论
@api_view(['POST'])
def update_user_score(request):
    record = GenerateRecord.objects.get(username=request.data['username'], index=request.data['index'])

    # 初始化分数
    record.select_score = 0
    record.judge_score = 0
    record.fill_score = 0
    record.calculate_score = 0
    record.essay_score = 0
    record.user_score = 0

    # 统计分数并更新数据库
    select_questions = SelectQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    record.select_score += get_score(select_questions, 'select')
    judge_questions = JudgeQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    record.judge_score += get_score(judge_questions, 'judge')
    fill_questions = FillQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    record.fill_score += get_score(fill_questions, 'fill')
    calculate_questions = CalculateQuestion.objects.filter(username=request.data['username'],
                                                           index=request.data['index'])
    record.calculate_score += get_score(calculate_questions, 'calculate')
    essay_questions = EssayQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    record.essay_score += get_score(essay_questions, 'essay')

    record.user_score = (record.select_score + record.judge_score + record.fill_score
                         + record.calculate_score + record.essay_score)

    # 获取评价
    if request.data['flag'] == 'yes':
        record.comment = get_record_comment(record.total_score, record.user_score)['comment']
    # 记录保存
    record.save()

    return APIResponse(code=0, message='批改结束')


@api_view(['GET'])
def get_user_score(request):
    try:
        if request.method == 'GET':
            user = request.GET.get('username')
            index = request.GET.get('index')
            record = GenerateRecord.objects.get(username=user, index=index)
            serializer = GenerateRecordSerializer(record)
            return APIResponse(code=0, msg='查询成功', data=serializer.data)
    except GenerateRecord.DoesNotExist:
        return APIResponse(code=0, msg='记录为空')
