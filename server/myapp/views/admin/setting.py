# Create your views here.

from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import Setting
from myapp.serializers import SettingSerializer

from myapp.utils import get_progress_mapping, get_next_progress, get_grade_unit


# 获取数据表中用户的题型设置数据
@api_view(['GET'])
def get_setting(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        setting = Setting.objects.get(username=user)
        serializer = SettingSerializer(setting)
        # print(serializer.data)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def get_progress(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        setting = Setting.objects.get(username=user)
        serializer = SettingSerializer(setting)
        grade, unit = get_grade_unit(serializer.data['progress'])
        data = {
            'grade': grade,
            'unit': unit,
        }
        return APIResponse(code=0, msg='查询成功', data=data)


# 更新题型选择
@api_view(['POST'])
def update_flag(request):
    setting = Setting.objects.get(username=request.data['username'])

    data = request.data.copy()
    data.update({
        'select_flag': request.data['select_flag'],
        'judge_flag': request.data['judge_flag'],
        'fill_flag': request.data['fill_flag'],
        'calculate_flag': request.data['calculate_flag'],
        'essay_flag': request.data['essay_flag'],
    })
    serializer = SettingSerializer(setting, data=data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return APIResponse(code=0, message='选择题型更新成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, message='更新失败')


# 更新各题型数量设置
@api_view(['POST'])
def update_quantity(request):
    setting = Setting.objects.get(username=request.data['username'])

    data = {'username': request.data['username']}
    que_type = request.data['type']
    data.update({
        que_type: request.data[que_type],
    })
    serializer = SettingSerializer(setting, data=data)

    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, message='更新成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, message='更新失败')


# 选择年级和单元后更新学习进度
@api_view(['POST'])
def update_progress(request):
    setting = Setting.objects.get(username=request.data['username'])

    data = {'username': request.data['username']}
    progress = get_progress_mapping(request.data['grade'], request.data['unit'])
    data.update({
        'progress': progress,
    })
    serializer = SettingSerializer(setting, data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, message='进度更新成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, message='更新失败')


# 进入下一阶段学习
@api_view(['POST'])
def update_next_progress(request):
    setting = Setting.objects.get(username=request.data['username'])
    old_grade, old_unit = setting.progress.split(', ')  # 旧进度

    data = {'username': request.data['username']}
    next_progress = get_next_progress(old_grade, old_unit)
    data.update({
        'progress': next_progress,
    })
    serializer = SettingSerializer(setting, data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, message='进度更新成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, message='更新失败')


@api_view(['POST'])
def update_selected_grade(request):
    setting = Setting.objects.get(username=request.data['username'])

    data = {'username': request.data['username']}
    data.update({
        'integrated_grade': request.data['integrated_grade'],
    })
    serializer = SettingSerializer(setting, data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, message='进度更新成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, message='更新失败')


@api_view(['POST'])
def reset_setting(request):
    setting = Setting.objects.get(username=request.data['username'])

    data = {'username': request.data['username']}
    data.update({
        'select_flag': True,
        'judge_flag': True,
        'fill_flag': True,
        'calculate_flag': True,
        'essay_flag': True,
        'select_quantity': 10,
        'judge_quantity': 6,
        'fill_quantity': 10,
        'calculate_quantity': 6,
        'essay_quantity': 6,
    })
    serializer = SettingSerializer(setting, data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, message='题型设置重置成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, message='更新失败')
