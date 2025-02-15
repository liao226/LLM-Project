"""
信息序列化函数
"""
from rest_framework import serializers

from myapp.models import (User, Setting, GenerateRecord,
                          SelectQuestion, JudgeQuestion, FillQuestion, CalculateQuestion, EssayQuestion)


class UserSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    login_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = User
        fields = '__all__'


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'


class GenerateRecordSerializer(serializers.ModelSerializer):
    generate_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = GenerateRecord
        fields = '__all__'


class SelectSerializer(serializers.ModelSerializer):
    generate_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = SelectQuestion
        fields = '__all__'


class JudgeSerializer(serializers.ModelSerializer):
    generate_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = JudgeQuestion
        fields = '__all__'


class FillSerializer(serializers.ModelSerializer):
    generate_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = FillQuestion
        fields = '__all__'


class CalculateSerializer(serializers.ModelSerializer):
    generate_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = CalculateQuestion
        fields = '__all__'


class EssaySerializer(serializers.ModelSerializer):
    generate_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = EssayQuestion
        fields = '__all__'
