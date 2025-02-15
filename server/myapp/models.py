"""
定义数据库表和和相应的字段类型
"""

from django.db import models


# 用户信息表
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    token = models.CharField(max_length=32, null=True)
    create_time = models.DateTimeField(max_length=6, null=True)
    login_time = models.DateTimeField(max_length=6, null=True)

    class Meta:
        # 数据库表名
        db_table = "user"


# 用户题型设置表
class Setting(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True)
    progress = models.CharField(max_length=50, null=True)
    integrated_grade = models.CharField(max_length=50, null=True)
    select_flag = models.BooleanField(default=True, null=True)
    select_quantity = models.IntegerField(default=10, null=True)
    judge_flag = models.BooleanField(default=True, null=True)
    judge_quantity = models.IntegerField(default=5, null=True)
    fill_flag = models.BooleanField(default=True, null=True)
    fill_quantity = models.IntegerField(default=10, null=True)
    calculate_flag = models.BooleanField(default=True, null=True)
    calculate_quantity = models.IntegerField(default=6, null=True)
    essay_flag = models.BooleanField(default=True, null=True)
    essay_quantity = models.IntegerField(default=6, null=True)

    class Meta:
        # 数据库表名
        db_table = "setting"


# 用户出题记录
class GenerateRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    index = models.CharField(max_length=255)
    # 题目范围
    question_range = models.CharField(max_length=255, null=True)
    # 得分换算成百分制后总分
    total_score = models.FloatField(default=0, null=True)
    user_score = models.FloatField(default=0, null=True)
    # 各题型得分
    select_score = models.FloatField(default=0, null=True)
    judge_score = models.FloatField(default=0, null=True)
    fill_score = models.FloatField(default=0, null=True)
    calculate_score = models.FloatField(default=0, null=True)
    essay_score = models.FloatField(default=0, null=True)
    # 总评
    comment = models.CharField(max_length=255, null=True)
    generate_time = models.DateTimeField(max_length=6, null=True)

    class Meta:
        # 数据库表名
        db_table = "generate_record"


# 所出选择题
class SelectQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=50, null=True)
    index = models.CharField(max_length=255, null=True)  # 第几次生成的结果
    generate_time = models.DateTimeField(max_length=6, null=True)
    solution = models.CharField(max_length=255, null=True)
    option_a = models.CharField(max_length=255, null=True)
    option_b = models.CharField(max_length=255, null=True)
    option_c = models.CharField(max_length=255, null=True)
    option_d = models.CharField(max_length=255, null=True)
    user_answer = models.CharField(max_length=255, null=True)
    flag = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)

    class Meta:
        # 数据库表名
        db_table = "select_question"


# 所出判断题
class JudgeQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=50, null=True)
    index = models.CharField(max_length=255, null=True)  # 第几次生成的结果
    generate_time = models.DateTimeField(max_length=6, null=True)
    solution = models.CharField(max_length=50, null=True)
    user_answer = models.CharField(max_length=50, null=True)
    flag = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)

    class Meta:
        # 数据库表名
        db_table = "judge_question"


class FillQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=50, null=True)
    index = models.CharField(max_length=255, null=True)  # 第几次生成的结果
    generate_time = models.DateTimeField(max_length=6, null=True)
    solution = models.CharField(max_length=255, null=True)
    user_answer = models.CharField(max_length=255, null=True)
    flag = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)

    class Meta:
        # 数据库表名
        db_table = "fill_question"


class CalculateQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=50, null=True)
    index = models.CharField(max_length=255, null=True)  # 第几次生成的结果
    generate_time = models.DateTimeField(max_length=6, null=True)
    solution = models.CharField(max_length=255, null=True)
    user_answer = models.CharField(max_length=255, null=True)
    flag = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)

    class Meta:
        # 数据库表名
        db_table = "calculate_question"


class EssayQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=50, null=True)
    index = models.CharField(max_length=255, null=True)  # 第几次生成的结果
    generate_time = models.DateTimeField(max_length=6, null=True)
    solution = models.CharField(max_length=255, null=True)
    user_answer = models.CharField(max_length=255, null=True)
    flag = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)

    class Meta:
        # 数据库表名
        db_table = "essay_question"


"""
class Thing(models.Model):
    STATUS_CHOICES = (
        ('0', '上架'),
        ('1', '下架'),
    )
    id = models.BigAutoField(primary_key=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='classification_thing')
    name = models.CharField(max_length=20, blank=True, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')

    class Meta:
        db_table = "b_thing"        
"""
