<template>
  <div class="page-view">
    <div class="setting">
      <!-- 年级选择 -->
      <span>年级：</span>
      <div class="select-grade">
        <label for="grade5-1" class="grade" :class="{ 'selected': selectedGrade === 'grade5-1' }">
          <input type="radio" id="grade5-1" value="grade5-1" v-model="selectedGrade">
          五年级上册
        </label>
        <label for="grade5-2" class="grade" :class="{ 'selected': selectedGrade === 'grade5-2' }">
          <input type="radio" id="grade5-2" value="grade5-2" v-model="selectedGrade">
          五年级下册
        </label>
        <label for="grade6-1" class="grade" :class="{ 'selected': selectedGrade === 'grade6-1' }">
          <input type="radio" id="grade6-1" value="grade6-1" v-model="selectedGrade">
          六年级上册
        </label>
        <label for="grade6-2" class="grade" :class="{ 'selected': selectedGrade === 'grade6-2' }">
          <input type="radio" id="grade6-2" value="grade6-2" v-model="selectedGrade">
          六年级下册
        </label>
        <!-- 生成按钮 -->
        <div>
          <a-button class="generate-button" size="large" @click="generate"> 生成</a-button>
        </div>
      </div>
      <!-- 分割线 -->
      <hr style="border-top: 1px solid #8a8f9f; margin-top: 12px;">
    </div>

    <!-- 题目显示区 -->
    <div>
      <!-- 选择题 -->
      <div class="questions">
        <span class="question-title">一、选择题（每题 2 分）</span>
        <a-empty class="empty" v-if="questions.selectList.length <=0 && !loading.selectLoading"></a-empty>
        <div v-if="settings.isSelectSelected">
          <div v-for="(question, index) in questions.selectList" :key="index">
            <!-- 题目 -->
            <p style="margin-left: 20px; margin-top: 15px; font-weight: normal;">{{ index + 1 }}. {{
                question.question
              }}</p>
            <!-- 选项 -->
            <div class="options" style="margin-left: 40px; display: flex; cursor: pointer;">
              <div
                  v-for="(option, key) in { 'A': question.option_a, 'B': question.option_b, 'C': question.option_c, 'D': question.option_d }"
                  :key="key"
                  style="flex: 0 0 20%; font-weight: normal; cursor: pointer;">
                <input type="radio" :id="`select_option${index}${key}`" :name="`select_question${index}`"
                       style=" cursor: pointer;"
                       @change="saveSelectAnswer(index, option)"
                       :checked="option === question.user_answer">
                <label :for="`select_option${index}${key}`" style="margin-left: 10px; cursor: pointer;">{{ key }}. {{
                    option
                  }}</label>
              </div>
            </div>
            <!-- 加载图标 -->
            <div class="load-icon" v-if="question.loading">
              <img :src="loading_img" class="loading" alt="">
            </div>
            <!-- 回答判断 -->
            <p class="judge-answer" v-if="question.flag === 'true' && question.comment">
              回答正确，答案为：{{ question.solution }}</p>
            <p class="judge-answer" v-if="question.flag === 'false' && question.comment">
              回答错误，答案为：{{ question.solution }}</p>
            <!-- 题目解析 -->
            <p class="question-comment" v-if="question.flag === 'true' || question.flag === 'false'">{{
                question.comment
              }}</p>
          </div>
          <div class="load-icon" v-if="loading.selectLoading">
            <img :src="loading_img" class="loading" alt="">
          </div>
        </div>
      </div>
      <!-- 判断题 -->
      <div class="questions">
        <span class="question-title">二、判断题（每题 2 分）</span>
        <a-empty class="empty" v-if="questions.judgeList.length <= 0 && !loading.judgeLoading"></a-empty>
        <div v-if="settings.isJudgeSelected">
          <div v-for="(question, index) in questions.judgeList" :key="index">
            <!-- 题目 -->
            <p style="margin-left: 20px; margin-top: 15px; font-weight: normal;">{{ index + 1 }}. {{
                question.question
              }}</p>
            <!-- 判断框 -->
            <div class="options" style="justify-content: flex-end; margin-right:200px; display: flex; cursor: pointer;">
              <div v-for="(option, key) in { '√': 'true', '×': 'false' }"
                   :key="key"
                   style="flex: 0 0 10%; font-weight: normal; cursor: pointer;">
                <input type="radio" :id="`judge_option${index}${key}`" :name="`judge_question${index}`"
                       style=" cursor: pointer;"
                       @change="saveJudgeAnswer(index, option)"
                       :checked="option === question.user_answer">
                <label :for="`judge_option${index}${key}`" style="margin-left: 8px; cursor: pointer;">{{ key }}</label>
              </div>
            </div>
            <!-- 加载图标 -->
            <div class="load-icon" v-if="question.loading">
              <img :src="loading_img" class="loading" alt="">
            </div>
            <!-- 回答判断 -->
            <p class="judge-answer" v-if="question.flag === 'true' && question.comment">
              回答正确，答案为：{{ question.solution }}</p>
            <p class="judge-answer" v-if="question.flag === 'false' && question.comment">
              回答错误，答案为：{{ question.solution }}</p>
            <!-- 题目解析 -->
            <p class="question-comment" v-if="question.flag === 'true' || question.flag === 'false'">{{
                question.comment
              }}</p>
          </div>
          <div class="load-icon" v-if="loading.judgeLoading">
            <img :src="loading_img" class="loading" alt="">
          </div>
        </div>
      </div>
      <!-- 填空题 -->
      <div class="questions">
        <span class="question-title">三、填空题（每题 2 分）</span>
        <a-empty class="empty" v-if="questions.fillList.length <= 0 && !loading.fillLoading"></a-empty>
        <div v-if="settings.isFillSelected">
          <div v-for="(question, index) in questions.fillList" :key="index">
            <!-- 题目 -->
            <p style="margin-left: 20px; margin-top: 15px; font-weight: normal;">{{ index + 1 }}. {{
                question.question
              }}</p>
            <!-- 输入框 -->
            <textarea style="margin-left: 40px; width: 300px; height: 40px; font-size: 16px; padding: 7px;"
                      placeholder="请输入你的答案" @input="saveFillAnswer(index, $event)"
                      v-model="question.user_answer"></textarea>
            <!-- 加载图标 -->
            <div class="load-icon" v-if="question.loading">
              <img :src="loading_img" class="loading" alt="">
            </div>
            <!-- 回答判断 -->
            <p class="judge-answer" v-if="question.flag === 'true' && question.comment">
              回答正确，答案为：{{ question.solution }}</p>
            <p class="judge-answer" v-if="question.flag === 'false' && question.comment">
              回答错误，答案为：{{ question.solution }}</p>
            <!-- 题目解析 -->
            <p class="question-comment" v-if="question.flag === 'true' || question.flag === 'false'">{{
                question.comment
              }}</p>
          </div>
          <div class="load-icon" v-if="loading.fillLoading">
            <img :src="loading_img" class="loading" alt="">
          </div>
        </div>
      </div>
      <!-- 计算题 -->
      <div class="questions">
        <span class="question-title">四、计算题（每题 2 分）</span>
        <a-empty class="empty" v-if="questions.calculateList.length <= 0 && !loading.calculateLoading"></a-empty>
        <div v-if="settings.isCalculateSelected">
          <div v-for="(question, index) in questions.calculateList" :key="index">
            <!-- 题目 -->
            <p style="margin-left: 20px; margin-top: 15px; font-weight: normal;">{{ index + 1 }}. {{
                question.question
              }}</p>
            <!-- 输入框 -->
            <textarea style="margin-left: 40px; width: 800px; height: 40px; font-size: 16px; padding: 7px;"
                      placeholder="请输入" @input="saveCalculateAnswer(index, $event)"
                      v-model="question.user_answer"></textarea>
            <!-- 加载图标 -->
            <div class="load-icon" v-if="question.loading">
              <img :src="loading_img" class="loading" alt="">
            </div>
            <!-- 回答判断 -->
            <p class="judge-answer" v-if="question.flag === 'true' && question.comment">
              回答正确，答案为：{{ question.solution }}</p>
            <p class="judge-answer" v-if="question.flag === 'false' && question.comment">
              回答错误，答案为：{{ question.solution }}</p>
            <!-- 题目解析 -->
            <p class="question-comment" v-if="question.flag === 'true' || question.flag === 'false'">{{
                question.comment
              }}</p>
          </div>
          <div class="load-icon" v-if="loading.calculateLoading">
            <img :src="loading_img" class="loading" alt="">
          </div>
        </div>
      </div>
      <!-- 应用题 -->
      <div class="questions">
        <span class="question-title">五、应用题（每题 6 分）</span>
        <a-empty class="empty" v-if="questions.essayList.length <= 0 && !loading.essayLoading"></a-empty>
        <div v-if="settings.isEssaySelected">
          <div v-for="(question, index) in questions.essayList" :key="index">
            <!-- 题目 -->
            <p style="margin-left: 20px; margin-top: 15px; font-weight: normal;">{{ index + 1 }}. {{
                question.question
              }}</p>
            <!-- 输入框 -->
            <textarea style="margin-left: 40px; width: 800px; height: 200px; font-size: 18px; padding: 10px;"
                      placeholder="请输入解答过程" @input="saveEssayAnswer(index, $event)"
                      v-model="question.user_answer"></textarea>
            <!-- 加载图标 -->
            <div class="load-icon" v-if="question.loading">
              <img :src="loading_img" class="loading" alt="">
            </div>
            <!-- 回答判断 -->
            <p class="judge-answer" v-if="question.flag === 'true' && question.comment">
              回答正确，答案为：{{ question.solution }}</p>
            <p class="judge-answer" v-if="question.flag === 'false' && question.comment">
              回答错误，答案为：{{ question.solution }}</p>
            <!-- 题目解析 -->
            <p class="question-comment" v-if="question.flag === 'true' || question.flag === 'false'">{{
                question.comment
              }}</p>
          </div>
          <div class="load-icon" v-if="loading.essayLoading">
            <img :src="loading_img" class="loading" alt="">
          </div>
        </div>
      </div>
      <!-- 得分和评价 -->
      <div style="margin-left: 30px; margin-top: 40px; font-size: 20px; font-weight: normal;"
           v-if="questions.comment">
        <p>得分：{{ questions.userScore }}</p>
        <p>总分：{{ questions.totalScore }}</p>
        <p>{{ questions.comment }}</p>
      </div>
      <!-- 提交按钮 -->
      <div style="display: flex; justify-content: flex-end; margin-top: 50px;">
        <a-button class="generate-button" size="large" @click="correct" style="margin-right: 30px;"> 提交
        </a-button>
        <a-popconfirm title="重做会清空之前的答题信息，确定要重做吗?" ok-text="确定" cancel-text="取消"
                      @confirm="reAnswer">
          <a-button class="generate-button" size="large" style="margin-right: 30px;"> 重答
          </a-button>
        </a-popconfirm>
        <a-button class="generate-button" size="large" @click="mistakeFeedback" style="margin-right: 30px;"> 错题反馈
        </a-button>
      </div>
      <div class="space" style="height: 200px;"></div>
    </div>
    <!-- 回到顶部 -->
    <div>
      <img :src="arrow" class="icon-arrow-up" alt="" @click="goToTop">
    </div>
  </div>

  <!-- 弹窗 -->
  <div>
    <a-modal
        :visible="modal.visible"
        :forceRender="true"
        :title="modal.title"
        @ok="handleOk"
        @cancel="handleCancel"
        width="60%"
        style="font-family: '楷体', KaiTi, serif;"
    >
      <!-- 题型选择 -->
      <p style="font-size: 18px;">请选择题型：</p>
      <div class="select-grade" style="font-size: 18px;">
        <label for="select" class="grade" :class="{ 'selected': modal.question_type === 'select' }">
          <input type="radio" id="select" value="select" v-model="modal.question_type">
          选择题
        </label>
        <label for="judge" class="grade" :class="{ 'selected': modal.question_type === 'judge' }">
          <input type="radio" id="judge" value="judge" v-model="modal.question_type">
          判断题
        </label>
        <label for="fill" class="grade" :class="{ 'selected': modal.question_type === 'fill' }">
          <input type="radio" id="fill" value="fill" v-model="modal.question_type">
          填空题
        </label>
        <label for="calculate" class="grade" :class="{ 'selected': modal.question_type === 'calculate' }">
          <input type="radio" id="calculate" value="calculate" v-model="modal.question_type">
          计算题
        </label>
        <label for="essay" class="grade" :class="{ 'selected': modal.question_type === 'essay' }">
          <input type="radio" id="essay" value="essay" v-model="modal.question_type">
          应答题
        </label>
      </div>
      <p style="font-size: 18px; margin-top: 20px;">请输入题号（题目前的序号）：</p>
      <input type="number"
             style="margin-left: 50px; width: 150px; height: 40px; font-size: 18px; border: 1px solid gray; padding: 8px; border-radius: 5px;"
             placeholder="请输入数字" v-model="modal.question_id"/>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import arrow from '/@/assets/icons/arrow-up-icon.png'
import loading_img from '/@/assets/icons/loading.png'
import {getSettingApi, updateSelectedGradeApi} from "/@/api/setting";
import {useUserStore} from "/@/store";
import {ref} from "vue";
import {message} from "ant-design-vue";
import {
  getIndexApi, addIndexApi,
} from "/@/api/record"
import {
  generateSelectApi, generateJudgeApi, generateFillApi, generateCalculateApi, generateEssayApi,
} from "/@/api/generate";
import {
  getSelectApi,
  getJudgeApi,
  getFillApi,
  getCalculateApi,
  getEssayApi,
  getMutiSelectApi,
  getMutiJudgeApi,
  getMutiFillApi,
  getMutiCalculateApi,
  getMutiEssayApi,
  updateSelectAnswerApi,
  updateJudgeAnswerApi,
  updateFillAnswerApi,
  updateCalculateAnswerApi,
  updateEssayAnswerApi,
  clearUserAnswerApi,
  deleteMistakeQuestionApi,
} from "/@/api/questions";
import {
  getUserScoreApi,
  updateCalculateCommentApi, updateEssayCommentApi,
  updateFillCommentApi,
  updateJudgeCommentApi,
  updateSelectCommentApi, updateTotalScoreApi, updateUserScoreApi
} from "/@/api/correct";

const userStore = useUserStore();

// 年级选择
const selectedGrade = ref();
watch(selectedGrade, () => {
  updateSelectedGradeApi({'username': userStore.user_name, 'integrated_grade': selectedGrade.value});
})

// 初始化选择的年级与进度一致，读取用户题型设置
onMounted(() => {
  getSetting();
  // 获取出题次数并初始化题目
  getIndexApi({username: userStore.user_name, question_type: '综合测试'}).then((res) => {
    index = res.data['index'];
    initData();
    // 更新总分，防止中意外导致总分不对
    updateTotalScoreApi({'username': userStore.user_name, 'index': index});
    updateUserScoreApi({'username': userStore.user_name, 'index': index});
    getUserScoreApi({username: userStore.user_name, index: index}).then((res) => {
      if (res.data) {
        questions.totalScore = res.data['total_score'];
        questions.userScore = res.data['user_score'];
        questions.comment = res.data['comment'];
      }
    });
  })
});

// 题目设置
const settings = ref({
  isSelectSelected: false,
  isJudgeSelected: false,
  isFillSelected: false,
  isCalculateSelected: false,
  isEssaySelected: false,
  selectQuantity: 0,
  judgeQuantity: 0,
  fillQuantity: 0,
  calculateQuantity: 0,
  essayQuantity: 0
});

const loading = ref({
  selectLoading: false,
  judgeLoading: false,
  fillLoading: false,
  calculateLoading: false,
  essayLoading: false,
});

let index: string;  // 出题次数

// 获取题型设置
const getSetting = () => {
  // 获取题目设置信息
  getSettingApi({
    username: userStore.user_name,
  }).then((res) => {
    selectedGrade.value = res.data['integrated_grade'];
    // 题型选择
    settings.value.isSelectSelected = res.data['select_flag'];
    settings.value.isJudgeSelected = res.data['judge_flag'];
    settings.value.isFillSelected = res.data['fill_flag'];
    settings.value.isCalculateSelected = res.data['calculate_flag'];
    settings.value.isEssaySelected = res.data['essay_flag'];
    // 数量设置
    settings.value.selectQuantity = res.data['select_quantity'];
    settings.value.judgeQuantity = res.data['judge_quantity'];
    settings.value.fillQuantity = res.data['fill_quantity'];
    settings.value.calculateQuantity = res.data['calculate_quantity'];
    settings.value.essayQuantity = res.data['essay_quantity'];
  }).catch((error) => {
    console.log(error);
  });
};

// 页面刷新初始化题目列表和用户答案
const initData = () => {
  getMutiSelectApi({username: userStore.user_name, index: index}).then((res) => {
    questions.selectList = questions.selectList.concat(res.data);
  });
  getMutiJudgeApi({username: userStore.user_name, index: index}).then((res) => {
    questions.judgeList = questions.judgeList.concat(res.data);
  });
  getMutiFillApi({username: userStore.user_name, index: index}).then((res) => {
    questions.fillList = questions.fillList.concat(res.data);
  });
  getMutiCalculateApi({username: userStore.user_name, index: index}).then((res) => {
    questions.calculateList = questions.calculateList.concat(res.data);
  });
  getMutiEssayApi({username: userStore.user_name, index: index}).then((res) => {
    questions.essayList = questions.essayList.concat(res.data);
  });
  getUserScoreApi({username: userStore.user_name, index: index}).then((res) => {
    if (res.data) {
      questions.totalScore = res.data['total_score'];
      questions.userScore = res.data['user_score'];
      questions.comment = res.data['comment'];
    }
  });
};

const questions = reactive({
  selectList: <any>[],
  judgeList: <any>[],
  fillList: <any>[],
  calculateList: <any>[],
  essayList: <any>[],
  userScore: undefined,
  totalScore: undefined,
  comment: undefined,
});

const userAnswer = reactive({
  selectList: {},
  judgeList: {},
  fillList: {},
  calculateList: {},
  essayList: {},
});

// 用户选择题和判断题答案保存
const saveSelectAnswer = (idx: any, option: string) => {
  userAnswer.selectList[idx + 1] = option;
  updateSelectAnswerApi({'username': userStore.user_name, 'index': index, 'answer': userAnswer.selectList});
}
const saveJudgeAnswer = (idx: any, option: any) => {
  userAnswer.judgeList[idx + 1] = option;
  updateJudgeAnswerApi({'username': userStore.user_name, 'index': index, 'answer': userAnswer.judgeList});
}
const saveFillAnswer = (idx: any, event: any) => {
  userAnswer.fillList[idx + 1] = event.target.value;
  updateFillAnswerApi({'username': userStore.user_name, 'index': index, 'answer': userAnswer.fillList});
}
const saveCalculateAnswer = (idx: any, event: any) => {
  userAnswer.calculateList[idx + 1] = event.target.value;
  updateCalculateAnswerApi({'username': userStore.user_name, 'index': index, 'answer': userAnswer.calculateList});
}
const saveEssayAnswer = (idx: any, event: any) => {
  userAnswer.essayList[idx + 1] = event.target.value;
  updateEssayAnswerApi({'username': userStore.user_name, 'index': index, 'answer': userAnswer.essayList});
}

// 清空题目列表
const clearQuestionList = () => {
  for (let key in questions) {
    if (Array.isArray(questions[key])) {
      questions[key] = [];
    }
  }
};

// 生成选择题
const generateSelect = async () => {
  loading.value.selectLoading = true;  // 加载中
  for (let i = 0; i < settings.value.selectQuantity; i++) {
    await generateSelectApi({
      'username': userStore.user_name,
      'index': index,
      'question_type': '综合测试',
      'grade': selectedGrade.value
    }).then(async () => {
      const res = await getSelectApi({username: userStore.user_name, index: index, question_idx: i});
      questions.selectList = questions.selectList.concat(res.data);
    });
  }
  loading.value.selectLoading = false;  // 加载结束
};

// 生成判断题
const generateJudge = async () => {
  loading.value.judgeLoading = true;
  for (let i = 0; i < settings.value.judgeQuantity; i++) {
    await generateJudgeApi({
      'username': userStore.user_name,
      'index': index,
      'question_type': '综合测试',
      'grade': selectedGrade.value
    }).then(async () => {
      const res = await getJudgeApi({username: userStore.user_name, index: index, question_idx: i});
      questions.judgeList = questions.judgeList.concat(res.data);
    });
  }
  loading.value.judgeLoading = false;
}

// 生成填空题
const generateFill = async () => {
  loading.value.fillLoading = true;
  for (let i = 0; i < settings.value.fillQuantity; i++) {
    await generateFillApi({
      'username': userStore.user_name,
      'index': index,
      'question_type': '综合测试',
      'grade': selectedGrade.value
    }).then(async () => {
      const res = await getFillApi({username: userStore.user_name, index: index, question_idx: i});
      questions.fillList = questions.fillList.concat(res.data);
    });
  }
  loading.value.fillLoading = false;
}

// 生成计算题
const generateCalculate = async () => {
  loading.value.calculateLoading = true;
  for (let i = 0; i < settings.value.calculateQuantity; i++) {
    await generateCalculateApi({
      'username': userStore.user_name,
      'index': index,
      'question_type': '综合测试',
      'grade': selectedGrade.value
    }).then(async () => {
      const res = await getCalculateApi({username: userStore.user_name, index: index, question_idx: i});
      questions.calculateList = questions.calculateList.concat(res.data);
    });
  }
  loading.value.calculateLoading = false;
}

// 生成应用题
const generateEssay = async () => {
  loading.value.essayLoading = true;
  for (let i = 0; i < settings.value.essayQuantity; i++) {
    await generateEssayApi({
      'username': userStore.user_name,
      'index': index,
      'question_type': '综合测试',
      'grade': selectedGrade.value
    }).then(async () => {
      const res = await getEssayApi({username: userStore.user_name, index: index, question_idx: i});
      questions.essayList = questions.essayList.concat(res.data);
    });
  }
  loading.value.essayLoading = false;
}

// 题目生成
const generateQuestions = async () => {
  try {
    if (settings.value.isSelectSelected) {
      await generateSelect();
    }
    if (settings.value.isJudgeSelected) {
      await generateJudge();
    }
    if (settings.value.isFillSelected) {
      await generateFill();
    }
    if (settings.value.isCalculateSelected) {
      await generateCalculate();
    }
    if (settings.value.isEssaySelected) {
      await generateEssay();
    }
    await updateTotalScoreApi({'username': userStore.user_name, 'index': index});
  } catch (error) {
    console.error(error);
  }
};

// 出题函数
const generate = () => {
  // 清除原来生成的题目
  clearQuestionList();
  // 更新出题次数
  addIndexApi({'username': userStore.user_name, 'question_type': '综合测试'}).then(() => {
    // 获取出题次数
    getIndexApi({username: userStore.user_name, question_type: '综合测试'}).then((res) => {
      console.log(res.data);
      index = res.data['index'];
      // 出题
      generateQuestions();
    })
  });
}

const clearCommentList = () => {
  for (let key in questions) {
    if (Array.isArray(questions[key])) {
      questions[key].forEach((item: { flag: string; comment: string; }) => {
        item.flag = '';
        item.comment = '';
      });
    }
  }
  questions.userScore = undefined;
  questions.totalScore = undefined;
  questions.comment = undefined;
}

const updateSelectComment = async () => {
  for (let i = 0; i < settings.value.selectQuantity; i++) {
    questions.selectList[i].loading = true;
    await updateSelectCommentApi({'username': userStore.user_name, 'index': index, 'question_idx': i}).then(() => {
      getSelectApi({username: userStore.user_name, index: index, question_idx: i}).then((res) => {
        questions.selectList[i].flag = res.data['flag'];
        questions.selectList[i].comment = res.data['comment'];
        questions.selectList[i].loading = false;
      });
    });
  }
}

const updateJudgeComment = async () => {
  for (let i = 0; i < settings.value.judgeQuantity; i++) {
    questions.judgeList[i].loading = true;
    await updateJudgeCommentApi({'username': userStore.user_name, 'index': index, 'question_idx': i}).then(() => {
      getJudgeApi({username: userStore.user_name, index: index, question_idx: i}).then((res) => {
        questions.judgeList[i].flag = res.data['flag'];
        questions.judgeList[i].comment = res.data['comment'];
        questions.judgeList[i].loading = false;
      });
    });
  }
}

const updateFillComment = async () => {
  for (let i = 0; i < settings.value.fillQuantity; i++) {
    questions.fillList[i].loading = true;
    await updateFillCommentApi({'username': userStore.user_name, 'index': index, 'question_idx': i}).then(() => {
      getFillApi({username: userStore.user_name, index: index, question_idx: i}).then((res) => {
        questions.fillList[i].flag = res.data['flag'];
        questions.fillList[i].comment = res.data['comment'];
        questions.fillList[i].loading = false;
      });
    });
  }
}

const updateCalculateComment = async () => {
  for (let i = 0; i < settings.value.calculateQuantity; i++) {
    questions.calculateList[i].loading = true;
    await updateCalculateCommentApi({'username': userStore.user_name, 'index': index, 'question_idx': i}).then(() => {
      getCalculateApi({username: userStore.user_name, index: index, question_idx: i}).then((res) => {
        questions.calculateList[i].flag = res.data['flag'];
        questions.calculateList[i].comment = res.data['comment'];
        questions.calculateList[i].loading = false;
      });
    });
  }
}

const updateEssayComment = async () => {
  for (let i = 0; i < settings.value.essayQuantity; i++) {
    questions.essayList[i].loading = true;
    await updateEssayCommentApi({'username': userStore.user_name, 'index': index, 'question_idx': i}).then(() => {
      getEssayApi({username: userStore.user_name, index: index, question_idx: i}).then((res) => {
        questions.essayList[i].flag = res.data['flag'];
        questions.essayList[i].comment = res.data['comment'];
        questions.essayList[i].loading = false;
      });
    });
  }
}

const correct = async () => {
  try {
    clearCommentList();  // 清空原有判题评论信息
    goToTop();  // 返回顶部
    // 判题
    if (settings.value.isSelectSelected) {
      await updateSelectComment();
    }
    if (settings.value.isJudgeSelected) {
      await updateJudgeComment();
    }
    if (settings.value.isFillSelected) {
      await updateFillComment();
    }
    if (settings.value.isCalculateSelected) {
      await updateCalculateComment();
    }
    if (settings.value.isEssaySelected) {
      await updateEssayComment();
    }
    // 打分
    await updateTotalScoreApi({'username': userStore.user_name, 'index': index});
    await updateUserScoreApi({'username': userStore.user_name, 'index': index});
    await getUserScoreApi({username: userStore.user_name, index: index}).then((res) => {
      if (res.data) {
        questions.totalScore = res.data['total_score'];
        questions.userScore = res.data['user_score'];
        questions.comment = res.data['comment'];
      }
    });
  } catch (error) {
    console.error(error);
  }
};

const reAnswer = () => {
  // 清空用户答案和得分，重新初始化题目数据
  clearUserAnswerApi({'username': userStore.user_name, 'index': index});
  location.reload();
}

const goToTop = () => {
  const contentContainer = document.querySelector('.ant-layout-content');
  if (contentContainer) {
    contentContainer.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
};

const controller = new AbortController();
window.addEventListener('beforeunload', () => {
  controller.abort();   // 切换页面时中断请求
});

// 错题反馈
const modal = reactive({
  visible: false,
  title: '错题反馈',
  question_type: '',
  question_id: undefined,
});

const mistakeFeedback = () => {
  // 重置modal设置
  modal.question_id = undefined;
  modal.question_type = '';
  modal.visible = true;
}

const handleCancel = () => {
  modal.visible = false;
}

const handleOk = () => {
  if (modal.question_id != undefined && modal.question_type != '') {
    deleteMistakeQuestionApi({
      'username': userStore.user_name,
      'index': index,
      'question_type': modal.question_type,
      'question_id': modal.question_id
    }).then(() => {
      modal.visible = false;
      message.success('错题删除成功！感谢您的反馈！');
      location.reload();
    });
  } else {
    message.warn('请选择错题题型，输入错题题号！');
  }
}

</script>

<style scoped lang="less">
.page-view {
  background: #d9e2f6;
  padding: 24px;
  display: flex;
  flex-direction: column;
  font-family: '楷体', KaiTi, serif;
  font-size: 18px;
  font-weight: 700;
}

.select-grade {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
  margin-left: 50px;
  color: #616680;

  .grade {
    flex: 0 0 18%;
    cursor: pointer;
  }
}

.selected {
  color: #1E90FF;
  font-size: 20px;
}

.select-grade input[type="radio"] {
  display: none;
}

.generate-button {
  width: 100px;
  font-weight: bold;
  color: #ffffff;
  background: #1E90FF;
}

.icon-arrow-up {
  width: 45px;
  height: 45px;
  position: fixed;
  right: 30px;
  bottom: 20px;
  cursor: pointer;
  transition: transform 0.3s; // 添加一个过渡效果
}

.icon-arrow-up:hover {
  transform: scale(1.1); // 鼠标悬停时放大图标
}

.icon-arrow-up:active {
  transform: scale(0.9); // 点击时缩小图标
}

.questions {
  margin-top: 40px;
  margin-left: 30px;

  .question-title {
    font-family: '楷体', KaiTi, serif;
    margin-top: 20px;
  }

  .empty {
    color: gray;
  }
}

// 加载效果
@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.load-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 30px;

  .loading {
    width: 25px;
    height: 25px;
    animation: rotate 4s ease-in-out infinite;
  }
}

.judge-answer {
  margin-left: 20px;
  margin-top: 15px;
  font-weight: normal;
  color: #ef4848;
  background: #fefefe;
  width: auto;
  padding: 5px;
  border-radius: 5px;
}

.question-comment {
  margin-left: 20px;
  font-weight: normal;
  color: #055081;
  background: #fefefe;
  padding: 8px;
  border-radius: 5px;
}
</style>
