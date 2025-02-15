# Create your views here.

from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import GenerateRecord, SelectQuestion, JudgeQuestion, FillQuestion, CalculateQuestion, EssayQuestion
from myapp.serializers import SelectSerializer, JudgeSerializer, FillSerializer, \
    CalculateSerializer, EssaySerializer
from myapp.utils import update_user_answer


# 获取第index次出题结果
@api_view(['GET'])
def get_select(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        question_id = request.GET.get('question_idx')

        select_questions = SelectQuestion.objects.filter(username=user, index=index).order_by('id')
        select_question = select_questions[int(question_id)]
        serializer = SelectSerializer(select_question)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_muti_select(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        select_questions = SelectQuestion.objects.filter(username=user, index=index).order_by('id')
        serializer = SelectSerializer(select_questions, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_judge(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        question_id = request.GET.get('question_idx')

        judge_questions = JudgeQuestion.objects.filter(username=user, index=index).order_by('id')
        judge_question = judge_questions[int(question_id)]
        serializer = JudgeSerializer(judge_question)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_muti_judge(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        judge_questions = JudgeQuestion.objects.filter(username=user, index=index).order_by('id')
        serializer = JudgeSerializer(judge_questions, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_fill(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        question_id = request.GET.get('question_idx')

        fill_questions = FillQuestion.objects.filter(username=user, index=index).order_by('id')
        fill_question = fill_questions[int(question_id)]
        serializer = FillSerializer(fill_question)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_muti_fill(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        fill_questions = FillQuestion.objects.filter(username=user, index=index).order_by('id')
        serializer = FillSerializer(fill_questions, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_calculate(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        question_id = request.GET.get('question_idx')

        calculate_questions = CalculateQuestion.objects.filter(username=user, index=index).order_by('id')
        calculate_question = calculate_questions[int(question_id)]
        serializer = CalculateSerializer(calculate_question)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_muti_calculate(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        calculate_questions = CalculateQuestion.objects.filter(username=user, index=index).order_by('id')
        serializer = CalculateSerializer(calculate_questions, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_essay(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        question_id = request.GET.get('question_idx')

        essay_questions = EssayQuestion.objects.filter(username=user, index=index).order_by('id')
        essay_question = essay_questions[int(question_id)]
        serializer = EssaySerializer(essay_question)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_muti_essay(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        index = request.GET.get('index')
        essay_questions = EssayQuestion.objects.filter(username=user, index=index).order_by('id')
        serializer = EssaySerializer(essay_questions, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
def update_select_answer(request):
    questions = SelectQuestion.objects.filter(username=request.data['username'], index=request.data['index']).order_by(
        'id')

    update_questions = update_user_answer(questions, request, False)

    for updated_question in update_questions:
        question = SelectQuestion.objects.get(id=updated_question['id'])
        question.user_answer = updated_question['user_answer']
        question.save()

    # 创建新的记录
    serializer = SelectSerializer(update_questions, many=True)
    return APIResponse(code=0, message='更新用户答案成功', data=serializer.data)


@api_view(['POST'])
def update_judge_answer(request):
    questions = JudgeQuestion.objects.filter(username=request.data['username'], index=request.data['index']).order_by(
        'id')

    update_questions = update_user_answer(questions, request, True)

    for updated_question in update_questions:
        question = JudgeQuestion.objects.get(id=updated_question['id'])
        question.user_answer = updated_question['user_answer']
        question.save()

    # 创建新的记录
    serializer = JudgeSerializer(update_questions, many=True)
    return APIResponse(code=0, message='更新用户答案成功', data=serializer.data)


@api_view(['POST'])
def update_fill_answer(request):
    questions = FillQuestion.objects.filter(username=request.data['username'], index=request.data['index']).order_by(
        'id')

    update_questions = update_user_answer(questions, request, False)

    for updated_question in update_questions:
        question = FillQuestion.objects.get(id=updated_question['id'])
        question.user_answer = updated_question['user_answer']
        question.save()

    # 创建新的记录
    serializer = FillSerializer(update_questions, many=True)
    return APIResponse(code=0, message='更新用户答案成功', data=serializer.data)


@api_view(['POST'])
def update_calculate_answer(request):
    questions = CalculateQuestion.objects.filter(username=request.data['username'],
                                                 index=request.data['index']).order_by('id')

    update_questions = update_user_answer(questions, request, False)

    for updated_question in update_questions:
        question = CalculateQuestion.objects.get(id=updated_question['id'])
        question.user_answer = updated_question['user_answer']
        question.save()

    serializer = CalculateSerializer(update_questions, many=True)
    return APIResponse(code=0, message='更新用户答案成功', data=serializer.data)


@api_view(['POST'])
def update_essay_answer(request):
    questions = EssayQuestion.objects.filter(username=request.data['username'], index=request.data['index']).order_by(
        'id')

    update_questions = update_user_answer(questions, request, False)

    for updated_question in update_questions:
        question = EssayQuestion.objects.get(id=updated_question['id'])
        question.user_answer = updated_question['user_answer']
        question.save()

    # 创建新的记录
    serializer = EssaySerializer(update_questions, many=True)
    return APIResponse(code=0, message='更新用户答案成功', data=serializer.data)


@api_view(['POST'])
def clear_user_answer(request):
    # 清空用户答案
    select_questions = SelectQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    for question in select_questions:
        question.user_answer = ''
        question.flag = ''
        question.save()

    judge_questions = JudgeQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    for question in judge_questions:
        question.user_answer = ''
        question.flag = ''
        question.save()

    fill_questions = FillQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    for question in fill_questions:
        question.user_answer = ''
        question.flag = ''
        question.save()

    calculate_questions = CalculateQuestion.objects.filter(username=request.data['username'],
                                                           index=request.data['index'])
    for question in calculate_questions:
        question.user_answer = ''
        question.flag = ''
        question.save()

    essay_questions = EssayQuestion.objects.filter(username=request.data['username'], index=request.data['index'])
    for question in essay_questions:
        question.user_answer = ''
        question.flag = ''
        question.save()

    # 清空上次出题记录中的评论
    record = GenerateRecord.objects.get(username=request.data['username'], index=request.data['index'])
    record.comment = ''
    record.save()

    return APIResponse(code=0, message='清空用户答案成功')


@api_view(['POST'])
def delete_mistake_question(request):
    question_type = request.data['question_type']
    question_id = int(request.data['question_id']) - 1
    if question_type == 'select':
        questions = SelectQuestion.objects.filter(username=request.data['username'],
                                                  index=request.data['index']).order_by('id')
        questions[question_id].delete()
    elif question_type == 'judge':
        questions = JudgeQuestion.objects.filter(username=request.data['username'],
                                                 index=request.data['index']).order_by('id')
        questions[question_id].delete()
    elif question_type == 'fill':
        questions = FillQuestion.objects.filter(username=request.data['username'],
                                                index=request.data['index']).order_by('id')
        questions[question_id].delete()
    elif question_type == 'calculate':
        questions = CalculateQuestion.objects.filter(username=request.data['username'],
                                                     index=request.data['index']).order_by('id')
        questions[question_id].delete()
    else:
        questions = EssayQuestion.objects.filter(username=request.data['username'],
                                                 index=request.data['index']).order_by('id')
        questions[question_id].delete()

    return APIResponse(code=0, message='错题删除成功')
