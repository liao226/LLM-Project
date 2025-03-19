# Create your views here.

from rest_framework.decorators import api_view

from myapp import utils
from myapp.handler import APIResponse
from myapp.models import (User, Setting, GenerateRecord, SelectQuestion, JudgeQuestion, FillQuestion,
                          CalculateQuestion, EssayQuestion)
from myapp.serializers import UserSerializer, SettingSerializer, GenerateRecordSerializer

from myapp.utils import md5value, get_avatar_message
from _datetime import datetime


# 用户登录
@api_view(['POST'])
def admin_login(request):
    username = request.data['username']
    password = utils.md5value(request.data['password'])
    users = User.objects.filter(username=username, password=password)
    if len(users) > 0:  # 存在符合条件的用户
        user = users[0]
        data = {
            'username': username,
            'password': password,
            'token': md5value(username),  # 生成令牌
            'login_time': datetime.now()  # 记录登录时间
        }
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse(code=0, message='登录成功', data=serializer.data)
        else:
            print(serializer.errors)

    return APIResponse(code=1, message='用户名或密码错误！')


# 用户注册
@api_view(['POST'])
def add_user(request):
    print(request.data)
    if not request.data.get('username', None) or not request.data.get('password', None):
        return APIResponse(code=1, message='用户名或密码不能为空')
    users = User.objects.filter(username=request.data['username'])
    if len(users) > 0:
        return APIResponse(code=1, message='该用户名已存在')

    # 默认用户题型设置
    setting_data = {
        'username': request.data['username'],
        'progress': 'grade5-1, unit1',  # 默认单元测试进度
        'integrated_grade': 'grade5-1',  # 默认综合测试进度
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
    }
    setting_serializer = SettingSerializer(data=setting_data)
    if setting_serializer.is_valid():
        setting_serializer.save()

    # 默认出题记录
    record_data = {
        'username': request.data['username'],
        'index': 0,
        'user_score': 0,
        'select_score': 0,
        'judge_score': 0,
        'fill_score': 0,
        'calculate_score': 0,
        'essay_score': 0
    }
    record_serializer = GenerateRecordSerializer(data=record_data)
    if record_serializer.is_valid():
        record_serializer.save()

    # 更新用户数据
    data = request.data.copy()
    data.update({
        'create_time': datetime.now(),
        'password': utils.md5value(request.data['password']),
    })
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, message='创建成功', data=serializer.data)
    else:
        print(serializer.errors)

    return APIResponse(code=1, message='创建失败')


# 修改密码
@api_view(['POST'])
def update_pwd(request):
    users = User.objects.filter(username=request.data['username'])
    if len(users) <= 0:
        return APIResponse(code=1, message='该用户名不存在')

    user = User.objects.get(username=request.data['username'])
    password = request.data.get('password', None)

    data = request.data.copy()
    data.update({'password': utils.md5value(password)})
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, message='密码修改成功', data=serializer.data)
    else:
        print(serializer.errors)

    return APIResponse(code=1, message='更新失败')


@api_view(['POST'])
def update_username(request):
    # 查找用户
    user = User.objects.get(username=request.data['username'])
    new_user = User.objects.filter(username=request.data['new_username'])

    if len(new_user) <= 0:  # 新账号名未注册
        # 更新设置表
        setting = Setting.objects.get(username=request.data['username'])
        setting.username = request.data['new_username']
        setting.save()
        # 更新出题记录
        GenerateRecord.objects.filter(username=request.data['username']).update(
            username=request.data['new_username'])
        # 更新题目表
        SelectQuestion.objects.filter(username=request.data['username']).update(username=request.data['new_username'])
        JudgeQuestion.objects.filter(username=request.data['username']).update(username=request.data['new_username'])
        FillQuestion.objects.filter(username=request.data['username']).update(username=request.data['new_username'])
        CalculateQuestion.objects.filter(username=request.data['username']).update(
            username=request.data['new_username'])
        EssayQuestion.objects.filter(username=request.data['username']).update(username=request.data['new_username'])

        # 更新用户表
        data = request.data.copy()
        data.update({'username': request.data['new_username']})
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse(code=0, message='账户名修改成功', data=serializer.data)
        else:
            print(serializer.errors)
    elif request.data['username'] == request.data['new_username']:  # 新账号名与旧账号相同
        return APIResponse(code=1, message='该用户名与旧用户名一致')
    else:
        return APIResponse(code=1, message='该用户名已存在')


@api_view(['POST'])
def delete_user(request):
    try:
        User.objects.filter(username=request.data['username']).delete()
        Setting.objects.filter(username=request.data['username']).delete()
        GenerateRecord.objects.filter(username=request.data['username']).delete()
        SelectQuestion.objects.filter(username=request.data['username']).delete()
        JudgeQuestion.objects.filter(username=request.data['username']).delete()
        FillQuestion.objects.filter(username=request.data['username']).delete()
        CalculateQuestion.objects.filter(username=request.data['username']).delete()
        EssayQuestion.objects.filter(username=request.data['username']).delete()

    except User.DoesNotExist:
        return APIResponse(code=1, message='对象不存在')

    return APIResponse(code=0, message='删除成功')


@api_view(['GET'])
def clickAvatar(request):
    data = get_avatar_message()
    return APIResponse(code=0, message='返回成功', data=data)
