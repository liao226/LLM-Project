from django.urls import path

from myapp import views

app_name = 'myapp'
# api
urlpatterns = [
    # 用户设置
    path('admin/adminLogin', views.admin.user.admin_login),  # 用户登录
    path('admin/user/add', views.admin.user.add_user),  # 新增用户
    path('admin/user/updatePwd', views.admin.user.update_pwd),  # 更新密码
    path('admin/user/updateUsername', views.admin.user.update_username),  # 更新账户名
    path('admin/user/deleteUser', views.admin.user.delete_user),  # 注销账户
    path('admin/user/clickAvatar', views.admin.user.clickAvatar),
    # 获取设置信息
    path('admin/setting/getSetting', views.admin.setting.get_setting),  # 题型设置信息
    path('admin/setting/getProgress', views.admin.setting.get_progress),  # 获取用户进度
    # 题型和进度更新
    path('admin/setting/updateFlag', views.admin.setting.update_flag),  # 更新题型设置
    path('admin/setting/updateQuantity', views.admin.setting.update_quantity),  # 更新各题型数量设置
    path('admin/setting/updateProgress', views.admin.setting.update_progress),  # 更新各题型数量设置
    path('admin/setting/updateNextProgress', views.admin.setting.update_next_progress),  # 更新到下一进度
    path('admin/setting/updateSelectedGrade', views.admin.setting.update_selected_grade),
    path('admin/setting/resetSetting', views.admin.setting.reset_setting),
    # 各类型出题函数
    path('admin/generate/generateSelect', views.admin.generate.generate_select),  # 选择题出题
    path('admin/generate/generateJudge', views.admin.generate.generate_judge),  # 判断题出题
    path('admin/generate/generateFill', views.admin.generate.generate_fill),  # 填空题出题
    path('admin/generate/generateCalculate', views.admin.generate.generate_calculate),  # 计算题出题
    path('admin/generate/generateEssay', views.admin.generate.generate_essay),  # 应答题出题
    # 各类型题目和答案获取
    path('admin/questions/getSelect', views.admin.questions.get_select),
    path('admin/questions/getMutiSelect', views.admin.questions.get_muti_select),
    path('admin/questions/getJudge', views.admin.questions.get_judge),
    path('admin/questions/getMutiJudge', views.admin.questions.get_muti_judge),
    path('admin/questions/getFill', views.admin.questions.get_fill),
    path('admin/questions/getMutiFill', views.admin.questions.get_muti_fill),
    path('admin/questions/getCalculate', views.admin.questions.get_calculate),
    path('admin/questions/getMutiCalculate', views.admin.questions.get_muti_calculate),
    path('admin/questions/getEssay', views.admin.questions.get_essay),
    path('admin/questions/getMutiEssay', views.admin.questions.get_muti_essay),
    # 用户答案的更新
    path('admin/questions/updateSelectAnswer', views.admin.questions.update_select_answer),
    path('admin/questions/updateJudgeAnswer', views.admin.questions.update_judge_answer),
    path('admin/questions/updateFillAnswer', views.admin.questions.update_fill_answer),
    path('admin/questions/updateCalculateAnswer', views.admin.questions.update_calculate_answer),
    path('admin/questions/updateEssayAnswer', views.admin.questions.update_essay_answer),
    path('admin/questions/clearUserAnswer', views.admin.questions.clear_user_answer),
    path('admin/questions/deleteMistakeQuestion', views.admin.questions.delete_mistake_question),
    # 出题次数的获取和更新
    path('admin/record/getIndex', views.admin.record.get_index),  # 获取出题次数记录
    path('admin/record/addIndex', views.admin.record.add_index),  # 更新出题次数记录
    # 出题记录获取和删除
    path('admin/record/getRecord', views.admin.record.get_record),
    path('admin/record/deleteRecord', views.admin.record.delete_record),
    # 用户答案判定和评语生成
    path('admin/correct/updateSelectComment', views.admin.correct.update_select_comment),  # 判断用户答案并生成解析
    path('admin/correct/updateJudgeComment', views.admin.correct.update_judge_comment),
    path('admin/correct/updateFillComment', views.admin.correct.update_fill_comment),
    path('admin/correct/updateCalculateComment', views.admin.correct.update_calculate_comment),
    path('admin/correct/updateEssayComment', views.admin.correct.update_essay_comment),
    path('admin/correct/updateTotalScore', views.admin.correct.update_total_score),
    path('admin/correct/updateUserScore', views.admin.correct.update_user_score),
    path('admin/correct/getUserScore', views.admin.correct.get_user_score),
]
