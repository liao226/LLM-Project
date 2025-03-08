from _datetime import datetime
import hashlib
import random
import json
import os


# 把密码转换成md5编码
def md5value(key):
    input_name = hashlib.md5()
    input_name.update(key.encode("utf-8"))
    md5str = (input_name.hexdigest()).lower()
    print('calculate md5:', md5str)
    return md5str


# 获取请求的IP
def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# 根据选择的年级和单元，得到符合格式的学习进度
def get_progress_mapping(grade, unit):
    """
    将年级和单元处理成规定格式的进度表示
    @param grade: 年级
    @param unit: 单元
    @return: 进度
    """
    mapping = {
        '一': 'unit1',
        '二': 'unit2',
        '三': 'unit3',
        '四': 'unit4',
        '五': 'unit5',
        '六': 'unit6',
        '七': 'unit7',
        '八': 'unit8',
    }
    return grade + ', ' + mapping[unit]


# 根据进度获取前端格式的年级和单元
def get_grade_unit(progress):
    grade, unit = progress.split(', ')
    mapping = {
        'unit1': '一',
        'unit2': '二',
        'unit3': '三',
        'unit4': '四',
        'unit5': '五',
        'unit6': '六',
        'unit7': '七',
        'unit8': '八',
    }
    return grade, mapping[unit]


# 获取下一阶段进度
def get_next_progress(grade, unit):
    """
    @param grade: 现年级
    @param unit: 现单元
    @return: 下一进度
    """
    # 五年级下册映射关系
    grade5_mapping = {
        'unit2': 'unit3',
        'unit3': 'unit4',
        'unit4': 'unit6',
        'unit6': 'unit8',
    }

    progress = ''
    if grade == 'grade5-1' and unit == 'unit7':  # 五年级上册最后一个单元
        progress = 'grade5-2, unit2'
    elif grade == 'grade5-1':  # 五年级上册其它单元
        progress = grade + ', unit' + str(int(unit[-1]) + 1)
    elif grade == 'grade5-2' and unit == 'unit8':  # 五年级下册最后一个单元
        progress = 'grade6-1, unit1'
    elif grade == 'grade5-2':  # 五年级下册其它单元
        progress = grade + ', ' + grade5_mapping[unit]
    elif grade == 'grade6-1' and unit == 'unit6':  # 六年级上册最后一个单元
        progress = 'grade6-2, unit1'
    elif grade == 'grade6-1' and unit == 'unit1':  # 六年级上册第一单元
        progress = 'grade6-1, unit3'
    elif grade == 'grade6-1':  # 六年级上册其它单元
        progress = grade + ', unit' + str(int(unit[-1]) + 1)
    elif grade == 'grade6-2' and unit == 'unit5':  # 六年级下册最后一个单元
        progress = 'grade5-1, unit1'
    elif grade == 'grade6-2':  # 六年级下册其它单元
        progress = grade + ', unit' + str(int(unit[-1]) + 1)

    return progress


# 读取数据库数据文件，知识点和随机抽取的题目
def read_data(setting, request):
    question_type = request.data['question_type']
    # 单元测试
    if question_type == '单元测试':
        root = os.getcwd() + '/myapp/dataset'
        grade, unit = setting.progress.split(', ')
        path = os.path.join(root, f'{grade}/{unit}.json')
        # print(path)
        with open(path, encoding='utf-8') as file:
            file_data = json.load(file)
        return path, file_data, file_data['common_topic'], random.sample(file_data['questions'], 5)
    # 综合测试
    else:
        root = os.getcwd() + '/myapp/dataset'
        grade = setting.integrated_grade
        grade_dir = os.path.join(root, grade)

        files = os.listdir(grade_dir)
        json_files = [file for file in files if file.endswith('.json')]
        selected_file = random.choice(json_files)
        path = os.path.join(grade_dir, selected_file)
        print(path)
        with open(path, encoding='utf-8') as file:
            file_data = json.load(file)
        return path, file_data, file_data['common_topic'], random.sample(file_data['questions'], 5)


# 将新出的题保存到数据库中
def save_data(path, file_data, response):
    last_id = file_data['questions'][-1]['id'] if file_data['questions'] else -1
    new_id = last_id + 1
    new_question = {
        'id': new_id,
        'question': response['question'],
        'solution': response['solution']
    }
    file_data['questions'].append(new_question)
    updated_json = json.dumps(file_data, indent=4, ensure_ascii=False)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(updated_json)


# 根据prompt获取response
def get_response(prompt):
    # noinspection PyUnresolvedReferences
    from openai import OpenAI
    client = OpenAI(api_key="sk-rzaxizbdkgiavgsvfrwleuhfmeiaqtmwmnerqlqheowvwknd",
                    base_url="https://api.siliconflow.cn/v1")

    # deepseek
    # client = OpenAI(api_key="sk-8536ff89b03c465b9538706bff34104f",
    #                base_url="https://api.deepseek.com")

    # 发送聊天请求
    response = client.chat.completions.create(
        model='deepseek-ai/DeepSeek-V2.5',
        # model='deepseek-reasoner',  # deepseek-r1
        # model='deepseek-chat',  # deepseek-v3
        messages=[
            {'role': 'user',
             'content': prompt}
        ],
    )
    return response


# 处理得到的response，添加更多的字段信息
def process_response(data, username, index):
    data = data[data.find('{'):data.find('}') + 1].strip()

    response = json.loads(data)
    response['username'] = username
    response['generate_time'] = datetime.now()
    response['index'] = int(index)
    return response


# 获取更新问题中用户答案后的数组
def update_user_answer(questions, request, isJudge):
    update_questions = []
    for i, question in enumerate(questions):
        ans_key = f'answer[{i + 1}]'
        # 存在对应用户答案
        if ans_key in request.data:
            data = question.__dict__.copy()
            if isJudge:
                data['user_answer'] = 'true' if request.data[ans_key] == 'true' else 'false'
            else:
                data['user_answer'] = request.data[ans_key]
        else:
            data = question.__dict__.copy()
        update_questions.append(data)
    return update_questions


def get_question_comment(question, solution, user_answer, comment):
    # noinspection PyUnresolvedReferences
    from openai import OpenAI
    client = OpenAI(api_key="sk-rzaxizbdkgiavgsvfrwleuhfmeiaqtmwmnerqlqheowvwknd",
                    base_url="https://api.siliconflow.cn/v1")

    # deepseek
    # client = OpenAI(api_key="sk-8536ff89b03c465b9538706bff34104f",
    #                base_url="https://api.deepseek.com")

    prompt = (
        f'有一道数学题，题目为{question}，该题记录的答案为{solution}，用户的答案为{user_answer}，题目的解析为{comment}，'
        f'要求返回的结果是一个字典，字典内容包括结合原有的解析，并且在原有解析的基础上进行修正，重新生成的新的解析“comment”，以及一个“flag”标记用户答案是否正确。'
        f'“comment”中说明题目的计算过程，解析格式为：“解析：...”，三个点的位置表示具体返回的解析。'
        f'如果用户答案只写了类似于“解：”“答：”的内容，而没有计算结果（指的是数字或文字表示的计算结果），应该判定为答案错误，flag的值为false。'
        f'如果用户的答案为空，或者用户的计算结果不正确，都判定为答案错误，flag的值为false。'
        f'对比用户的答案和题目答案，如果用户的答案表达的意思与题目答案一致，则“flag”的值为字符串true，否则“flag”值为字符串false，字符串字母均为小写。'
        f'另外，在生成的解析中说明为什么这样判断用户的答案。'
        f'仅返回一个字典，不需要添加任何额外的文字，也不需要保留任何类似json或python的格式提示字段和说明。'
    )

    # 发送聊天请求
    response = client.chat.completions.create(
        model='deepseek-ai/DeepSeek-V2.5',
        # model='deepseek-reasoner',  # deepseek-r1
        # model='deepseek-chat',  # deepseek-v3
        messages=[
            {'role': 'user',
             'content': prompt}
        ],
    )
    data = response.choices[0].message.content
    data = data[data.find('{'):data.find('}') + 1].strip()

    data = json.loads(data)
    # 修正部分答案判定
    if user_answer == solution:
        data['flag'] = 'true'
    if (user_answer is None or user_answer == '解：' or user_answer == '答：' or user_answer == '解' or user_answer == '答'
            or user_answer == ''):
        data['flag'] = 'false'
        print(data)

    return data


def get_score(questions, mode):
    if mode == 'essay':
        single_score = 6
    else:
        single_score = 2
    score = 0
    for question in questions:
        if question.flag == 'true':
            score += single_score
    return score


def get_record_comment(total_score, user_score):
    # noinspection PyUnresolvedReferences
    from openai import OpenAI
    client = OpenAI(api_key="sk-rzaxizbdkgiavgsvfrwleuhfmeiaqtmwmnerqlqheowvwknd",
                    base_url="https://api.siliconflow.cn/v1")

    # deepseek
    # client = OpenAI(api_key="sk-8536ff89b03c465b9538706bff34104f",
    #                base_url="https://api.deepseek.com")

    prompt = (
        f'有一份数学试卷，试卷题目的总分为{total_score}，用户做答的得分为{user_score}。'
        f'要求返回的形式是一个字典，评论对应的键为comment，内容为评论。'
        f'要求结合试卷总分和用户总分，大致计算出用户答题的准确率，然后在评论中体现出用户答题的准确率，并再生成几句鼓励性的评语，评语大概控制在三四句左右，'
        f'鼓励用户继续努力，或者在用户准备率很高（大致准确率达到80%及以上），对用户进行夸奖什么的。'
        f'仅返回一个字典，不需要添加任何额外的文字，也不需要保留任何类似json或python的格式提示字段和说明。'
    )

    # 发送聊天请求
    response = client.chat.completions.create(
        model='deepseek-ai/DeepSeek-V2.5',
        # model='deepseek-reasoner',  # deepseek-r1
        # model='deepseek-chat',  # deepseek-v3
        messages=[
            {'role': 'user',
             'content': prompt}
        ],
    )
    data = response.choices[0].message.content
    data = data[data.find('{'):data.find('}') + 1].strip()

    data = json.loads(data)

    return data


def convert_question_range(progress):
    grade_map = {
        'grade5-1': '五年级上册',
        'grade5-2': '五年级下册',
        'grade6-1': '六年级上册',
        'grade6-2': '六年级下册'
    }
    unit_map = {
        'unit1': '一',
        'unit2': '二',
        'unit3': '三',
        'unit4': '四',
        'unit5': '五',
        'unit6': '六',
        'unit7': '七',
        'unit8': '八',
    }
    # 综合测试
    if len(progress) == 1:
        return grade_map[progress[0]]
    # 单元测试
    else:
        return grade_map[progress[0]] + f'，第{unit_map[progress[1]]}单元'


# 生成点击头像后的信息
def get_avatar_message():
    # noinspection PyUnresolvedReferences
    from openai import OpenAI
    client = OpenAI(api_key="sk-rzaxizbdkgiavgsvfrwleuhfmeiaqtmwmnerqlqheowvwknd",
                    base_url="https://api.siliconflow.cn/v1")

    # deepseek
    # client = OpenAI(api_key="sk-8536ff89b03c465b9538706bff34104f",
    #                base_url="https://api.deepseek.com")

    prompt = (
        f'有一个场景是用户点击一个网页的头像，该网页没有做头像更换的功能，所以希望可以返回一个调皮一点、活泼一点的信息来进行用户反馈，可以参考下面几句信息：'
        f'[“没有了哦”，“真的没有啦！”，“真的真的没有啦！”，“今天也要开心哦”，“发现你在偷懒咯”，“好好学习，天天向上”，“再点就要生气啦”，'
        f'“嘘，偷偷告诉你，妈妈在你后面”，“今天也要好好学习”，“累了就去休息叭”，“我今天也在等你哦”，“你爱学习！”]'
        f'请生成这样的一句信息，并将回答以字典的形式进行返回，回答对应的键为“message”。'
        f'生成类似这样的带有祝福性质或轻松玩笑性质的信息。'
        f'仅返回一个字典，不需要添加任何额外的文字，也不需要保留任何类似json或python的格式提示字段和说明。'
    )

    # 发送聊天请求
    response = client.chat.completions.create(
        model='deepseek-ai/DeepSeek-V2.5',
        # model='deepseek-reasoner',  # deepseek-r1
        # model='deepseek-chat',  # deepseek-v3
        messages=[
            {'role': 'user', 'content': prompt}
        ],
    )
    data = response.choices[0].message.content
    data = data[data.find('{'):data.find('}') + 1].strip()
    data = json.loads(data)
    print(data)
    return data
