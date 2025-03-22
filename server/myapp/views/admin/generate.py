# Create your views here.
import random

from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import Setting
from myapp.serializers import SelectSerializer, JudgeSerializer, FillSerializer, \
    CalculateSerializer, EssaySerializer
from myapp.utils import read_data, save_data, get_response, process_response


# 出题
@api_view(['POST'])
def generate_select(request):
    while True:
        try:
            # 用户设置
            setting = Setting.objects.get(username=request.data['username'])
            file_path, file_data, topic, questions = read_data(setting, request)

            # 选择题
            select_prompt = (
                f'假如你是一名小学数学老师，你幽默风趣，认真教学，喜欢鼓励和夸奖学生帮助学生进步。你希望出几道题目帮助学生学习，在生成题目答案的过程，'
                f'你会反复验算核对以保证题目的解析和答案是正确的'
                f'有数学知识点{topic}，该知识点有几道相应的题目及其答案{questions}。请根据这个知识点，以及和该知识点有关的这几道数学题目{questions}，'
                f'另外出一道与例题难度类似的数学题，但是希望出的题目要有变通，不是简单的替换题目中的物品和数据。返回的回答全部使用gbk编码方式编码。'
                f'要求题目中如果涉及类似于书本等不可拆分成小数份的物品，就不要写成小数份的，例如不能有0.8本书这样的描述。'
                f'但是像水果、蔬菜、水电这样不一定要求是整数的，就可以有相应的小数的表示。'
                f'要求题目的格式为字典形式，字典的键和值均用双引号包裹，返回的字典包含的键值包括所出的题目“question”，'
                f'题目解析字段“comment”，对应的值为一段文字对这道题目进行解析的文字，说明题目的计算过程，格式为：“解析：...”。三个点的位置表示具体返回的解析。'
                f'另外结合题目解析，返回的字典中包含正确答案“solution”，“solution”的值只保留计算答案，不包括计算过程和做答过程。'
                f'要求返回的字典的键还包括四个选项分别为[option_a, option_b, option_c, option_d]。'
                f'要求生成一个正确答案，另外生成三个与正确答案相似但不同的结果，将正确答案和三个干扰项共四个值前面四个选项中，作为选项字典键对应的值。'
                f'同时要求选项的值只包含计算结果，而不是包括计算的式子和过程，也不包括做答。'
                f'仅返回一个字典，不需要添加任何额外的文字，也不需要保留任何类似json或python的格式提示字段和说明。'
            )
            response = get_response(select_prompt)

            data = response.choices[0].message.content
            select_response = process_response(data, request.data['username'], request.data['index'])

            # 打乱四个选项对应的值
            option_values = [select_response['option_a'], select_response['option_b'], select_response['option_c'],
                             select_response['option_d']]
            random.shuffle(option_values)
            select_response['option_a'], select_response['option_b'], select_response['option_c'], select_response[
                'option_d'] = option_values

            select_serializer = SelectSerializer(data=select_response)
            if select_serializer.is_valid():
                select_serializer.save()
                return APIResponse(code=0, message='选择题出题成功', data=select_serializer.data)
        except Exception as e:
            print(f"Error occurred: {e}")
            continue


@api_view(['POST'])
def generate_judge(request):
    while True:
        try:
            # 用户设置
            setting = Setting.objects.get(username=request.data['username'])
            file_path, file_data, topic, questions = read_data(setting, request)

            # 判断题
            judge_prompt = (
                f'假如你是一名小学数学老师，你幽默风趣，认真教学，喜欢鼓励和夸奖学生帮助学生进步。你希望出几道题目帮助学生学习，在生成题目答案的过程，'
                f'你会反复验算核对以保证题目的答案是正确的。'
                f'有数学知识点{topic}，该知识点有几道相应的题目及其答案{questions}。请根据这个知识点，以及和该知识点有关的这几道数学题目{questions}，'
                f'另外出一道与例题难度类似的数学判断题，但是希望出的题目要有点变通，不要太单一，且题目不是问句。返回的回答全部使用gbk编码方式编码。'
                f'要求题目中如果涉及类似于书本等不可拆分成小数份的物品，就不要写成小数份的，例如不能有0.8本书、0.5张凳子这样的描述。'
                f'但是像水果、蔬菜、水电这样不一定要求是整数的，就可以有相应的小数的表示。'
                f'要求题目的格式为字典形式，字典的键和值均用双引号包裹，返回的字典包含的键值包括所出的题目question，'
                f'题目解析字段“comment”，对应的值为一段文字对这道题目进行解析的文字，说明题目的计算过程，格式为：“解析：...”。三个点的位置表示具体返回的解析。'
                f'另外结合题目解析，返回的字典中包含正确答案“solution”。如果题目正确，则“solution”的值为字符串“true”，'
                f'判断题题目错误则“solution”值为字符串“false”，均用小写字母表示。'
                f'要求出的题目里面如果涉及计算过程，则直接用计算结果表示，不需要将计算过程一起展示。'
                f'仅返回一个字典，不需要添加任何额外的文字，也不需要保留任何类似json或python的格式提示字段和说明。'
            )
            # 发送聊天请求
            response = get_response(judge_prompt)

            data = response.choices[0].message.content
            judge_response = process_response(data, request.data['username'], request.data['index'])

            judge_serializer = JudgeSerializer(data=judge_response)
            if judge_serializer.is_valid():
                judge_serializer.save()
                return APIResponse(code=0, message='判断题出题成功', data=judge_serializer.data)
        except Exception as e:
            print(f"Error occurred: {e}")
            continue


@api_view(['POST'])
def generate_fill(request):
    while True:
        try:
            # 用户设置
            setting = Setting.objects.get(username=request.data['username'])

            # 读取题库数据
            file_path, file_data, topic, questions = read_data(setting, request)

            # 填空题
            fill_prompt = (
                f'假如你是一名小学数学老师，你幽默风趣，认真教学，喜欢鼓励和夸奖学生帮助学生进步。你希望出几道题目帮助学生学习，在生成题目答案的过程，'
                f'你会反复验算核对以保证题目的答案是正确的。'
                f'有数学知识点{topic}，该知识点有几道相应的题目及其答案{questions}。请根据这个知识点，以及和该知识点有关的这几道数学题目{questions}，'
                f'另外出一道与例题难度类似的只需要填一个空的数学填空题，但是希望出的题目要有点变通，不要太单一。返回的回答全部使用gbk编码方式编码。'
                f'要求题目中如果涉及类似于书本等不可拆分成小数份的物品，就不要写成小数份的，例如不能有0.8本书这样的描述。'
                f'但是像水果、蔬菜、水电这样不一定要求是整数的，就可以有相应的小数的表示。'
                f'要求题目的格式为字典形式，字典的键和值均用双引号包裹，回答包含字段“comment”，该字段存放对题目的解析，对应的值为一段文字对这道题目进行解析的文字，'
                f'说明题目的计算过程，格式为：“解析：...”，三个点的位置表示具体返回的解析。'
                f'返回的字典包含的键值还包括所出的题目“question”，以及结合题目解析得到的所出的题目的答案“solution”。'
                f'要求题目中在需要填空的地方用“(  )”表示，提示这里需要填空，题目不要是问句，且只有一个位置需要进行填空。'
                f'题目对应需要填入的答案保存在“solution”字段里，答案只包括结果，不包括计算过程和解答过程。'
                f'生成的题目里不要两个小括号连在一起，即类似于“()()”这样的结构，也不需要给题目中的单位额外加括号，如(kg)要去掉kg外面的括号。'
                f'仅返回一个字典，不需要添加任何额外的文字，也不需要保留任何类似json或python的格式提示字段和说明。'
            )
            # 发送聊天请求
            response = get_response(fill_prompt)

            data = response.choices[0].message.content
            fill_response = process_response(data, request.data['username'], request.data['index'])

            fill_serializer = FillSerializer(data=fill_response)
            if fill_serializer.is_valid():
                fill_serializer.save()
                return APIResponse(code=0, message='填空题出题成功', data=fill_serializer.data)
        except Exception as e:
            print(f"Error occurred: {e}")
            continue


@api_view(['POST'])
def generate_calculate(request):
    while True:
        try:
            # 用户设置
            setting = Setting.objects.get(username=request.data['username'])
            file_path, file_data, topic, questions = read_data(setting, request)

            # 选择题
            calculate_prompt = (
                f'假如你是一名小学数学老师，你幽默风趣，认真教学，喜欢鼓励和夸奖学生帮助学生进步。你希望出几道题目帮助学生学习，在生成题目答案的过程，'
                f'你会反复验算核对以保证题目的答案是正确的。'
                f'有数学知识点{topic}，请根据这个知识点，出一道与例题难度类似的数学计算题。'
                f'要求题目的格式为字典形式，字典的键和值均用双引号包裹，返回的回答全部使用gbk编码方式编码。'
                f'返回的字典包含的键值包括所出的题目“question”，题目解析字段“comment”，“comment”对应的值为一段文字对这道题目进行解析的文字，'
                f'说明题目的计算过程，格式为：“解析：...”，三个点的位置表示具体返回的解析内容。'
                f'结合题目解析，返回字典里包含所出的题目的答案“solution”。'
                f'要求题目为一道计算式子，例如如果知识点是小数乘法，那么题目是根据知识点出类似于“7.01*2.6=”、“2.52/1.1=”这样的四则计算题，'
                f'而不是用一大段文字表述的数学场景应用题，需要是出一道计算，再加上一个等于号要求用户进行计算求解，可以混合使用四则运算出题。'
                f'如果题目知识点涉及解方程，那么题目可以是一道需要解方程的方程式。'
                f'结合解析“comment”，返回的字典中题目的答案保存在“solution”字段里，答案主要包括计算结果，不包括计算过程和解答过程。'
                f'仅返回一个字典，不需要添加任何额外的文字，也不需要保留任何类似json或python的格式提示字段和说明。'
            )
            # 发送聊天请求
            response = get_response(calculate_prompt)

            data = response.choices[0].message.content
            calculate_response = process_response(data, request.data['username'], request.data['index'])

            calculate_serializer = CalculateSerializer(data=calculate_response)
            if calculate_serializer.is_valid():
                calculate_serializer.save()
                return APIResponse(code=0, message='计算题出题成功', data=calculate_serializer.data)
        except Exception as e:
            print(f"Error occurred: {e}")
        continue


@api_view(['POST'])
def generate_essay(request):
    while True:
        try:
            # 用户设置
            setting = Setting.objects.get(username=request.data['username'])
            file_path, file_data, topic, questions = read_data(setting, request)

            # 选择题
            essay_prompt = (
                f'假如你是一名小学数学老师，你幽默风趣，认真教学，喜欢鼓励和夸奖学生帮助学生进步。你希望出几道题目帮助学生学习，在生成题目答案的过程，'
                f'你会反复验算核对以保证题目的答案是正确的。'
                f'有数学知识点{topic}，该知识点有几道相应的题目及其答案{questions}。请根据这个知识点，以及和该知识点有关的这几道数学题目{questions}，'
                f'另外出一道与例题难度类似的数学应用题，但是希望出的题目要有点变通，不要太单一。返回的回答全部使用gbk编码方式编码。'
                f'要求题目的格式为字典形式，字典的键和值均用双引号包裹，返回的字典包含的键值包括所出的题目“question”。'
                f'要求题目中如果涉及类似于书本等不可拆分成小数份的物品，就不要写成小数份的，例如不能有0.8本书这样的描述。'
                f'但是像水果、蔬菜、水电这样不一定要求是整数的，就可以有相应的小数的表示。'
                f'返回的结果包含字段“comment”，表示题目的解析，对应的值为一段文字对这道题目进行解析的文字，说明题目的计算过程，'
                f'解析格式为：“解析：...”，三个点的位置表示具体返回的解析。'
                f'结合解析的内容，返回的结果中还需要包括题目的答案“solution”，对应的值为所出的题目的答案，包括计算过程和计算结果。'
                f'仅返回一个字典，不需要添加任何额外的文字，也不需要保留任何类似json或python的格式提示字段和说明。'
            )
            # 发送聊天请求
            response = get_response(essay_prompt)

            data = response.choices[0].message.content
            essay_response = process_response(data, request.data['username'], request.data['index'])

            # 将生成的题目保存到原数据库中
            # save_data(file_path, file_data, essay_response)

            essay_serializer = EssaySerializer(data=essay_response)
            if essay_serializer.is_valid():
                essay_serializer.save()
                return APIResponse(code=0, message='应用题出题成功', data=essay_serializer.data)
        except Exception as e:
            print(f"Error occurred: {e}")
            continue
