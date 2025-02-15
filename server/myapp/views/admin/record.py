# Create your views here.

from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import GenerateRecord, Setting
from myapp.models import SelectQuestion, JudgeQuestion, FillQuestion, CalculateQuestion, EssayQuestion
from myapp.serializers import GenerateRecordSerializer

from myapp.utils import convert_question_range
from _datetime import datetime


# 获取出题次数（出题记录中index最大的记录）
@api_view(['GET'])
def get_index(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        question_type = request.GET.get('question_type')
        try:
            record = GenerateRecord.objects.filter(username=user, question_range__contains=question_type).order_by(
                '-id').first()
            serializer = GenerateRecordSerializer(record)
            return APIResponse(code=0, msg='查询成功', data=serializer.data)
        except GenerateRecord.DoesNotExist:
            # 返回 index=0 的记录
            record = GenerateRecord.objects.filter(username=user).order_by('id').first()
            serializer = GenerateRecordSerializer(record)
            return APIResponse(code=0, msg='查询成功', data=serializer.data)


# 新增出题记录
@api_view(['POST'])
def add_index(request):
    setting = Setting.objects.get(username=request.data['username'])

    if request.data['question_type'] == '单元测试':
        convert_progress = '【单元测试】 ' + convert_question_range(setting.progress.split(', '))
    else:
        convert_progress = '【综合测试】 ' + convert_question_range([setting.progress.split(', ')[0]])

    # 新增用户出题记录
    record = GenerateRecord.objects.filter(username=request.data['username']).order_by('-id').first()
    record_data = {
        'username': request.data['username'],
        'index': str(int(record.index) + 1),
        'question_range': convert_progress,
        'generate_time': datetime.now(),
    }
    record_serializer = GenerateRecordSerializer(data=record_data)

    if record_serializer.is_valid():
        record_serializer.save()
        return APIResponse(code=0, msg='查询成功', data=record_serializer.data)


@api_view(['GET'])
def get_record(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        keyword = request.GET.get('keyword')
        essay_questions = GenerateRecord.objects.filter(username=user, question_range__contains=keyword).order_by('-id')
        serializer = GenerateRecordSerializer(essay_questions, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
def delete_record(request):
    idxs = [int(num) for num in request.data['ids'].split(',')]
    try:
        # 删除出题记录和对应的题目
        for idx in idxs:
            if idx != 0:
                GenerateRecord.objects.get(username=request.data['username'], index=idx).delete()
                SelectQuestion.objects.filter(username=request.data['username'], index=idx).delete()
                JudgeQuestion.objects.filter(username=request.data['username'], index=idx).delete()
                FillQuestion.objects.filter(username=request.data['username'], index=idx).delete()
                CalculateQuestion.objects.filter(username=request.data['username'], index=idx).delete()
                EssayQuestion.objects.filter(username=request.data['username'], index=idx).delete()
    except GenerateRecord.DoesNotExist:
        return APIResponse(code=1, message='对象不存在')

    return APIResponse(code=0, message='删除成功')
