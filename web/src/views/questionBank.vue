<template>
  <!-- 页面区域 -->
  <div class="page-view">
    <!-- 删除键和搜索框 -->
    <div class="header">
      <span class="page-title">生成记录</span>
      <a-space class="table-operations">
        <!-- 批量删除按钮 -->
        <a-button class="deleteButton" size="large" @click="handleBatchDelete">批量删除</a-button>
        <!-- 搜索框 -->
        <a-input-search addon-before="题目范围" size="large" enter-button @search="onSearch" @change="onSearchChange"
        />
      </a-space>
    </div>
    <!-- 题目记录 -->
    <a-table
        size="large"
        rowKey="id"
        :loading="data.loading"
        :columns="columns"
        :data-source="data.recordList"
        :scroll="{ x: 'max-content' }"
        :row-selection="rowSelection"
        :pagination="{
          size: 'default',
          current: data.page,
          pageSize: data.pageSize,
          onChange: (current) => (data.page = current),
          showSizeChanger: false,
          showTotal: (total) => `共${total}条数据`,
        }"
    >
      <template #bodyCell="{ text, record, index, column }">
        <!-- 序号 -->
        <template v-if="column.key === 'id'">
          <span>{{ record.id }}</span>
        </template>
        <!-- 题目范围 -->
        <template v-if="column.key === 'question_range'">
          <span>{{ record.question_range }}</span>
        </template>
        <!-- 生成时间 -->
        <template v-if="column.key === 'generate_time'">
          <span>{{ record.generate_time }}</span>
        </template>
        <!-- 得分 -->
        <template v-if="column.key === 'user_score'">
          <span>{{ record.user_score }}</span>
        </template>
        <!-- 总分 -->
        <template v-if="column.key === 'total_score'">
          <span>{{ record.total_score }}</span>
        </template>
        <!-- 操作 -->
        <template v-if="column.key === 'operation'">
            <span>
              <a @click="handleView(record.question_range, record.index)">查看</a>
              <a-divider type="vertical"/>
              <a-popconfirm title="确定删除?" ok-text="是" cancel-text="否" @confirm="confirmDelete(record)">
                <a href="#">删除</a>
              </a-popconfirm>
            </span>
        </template>
      </template>
    </a-table>
  </div>

  <!-- 弹窗区域 -->
  <div>
    <a-modal
        :visible="modal.visible"
        :forceRender="true"
        :title="modal.title"
        @cancel="handleExit"
        :footer="null"
        width="90%"
        style="font-family: '楷体', KaiTi, serif;"
    >
      <!-- 题目显示区 -->
      <div class="modal" ref="modalContent">
        <!-- 选择题 -->
        <div class="questions" style="margin-top: 10px;">
          <span class="question-title">一、选择题（每题 2 分）</span>
          <a-empty class="empty" v-if="questions.selectList.length <=0"></a-empty>
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
        </div>
        <!-- 判断题 -->
        <div class="questions">
          <span class="question-title">二、判断题（每题 2 分）</span>
          <a-empty class="empty" v-if="questions.judgeList.length <= 0"></a-empty>
          <div v-for="(question, index) in questions.judgeList" :key="index">
            <!-- 题目 -->
            <p style="margin-left: 20px; margin-top: 15px; font-weight: normal;">{{ index + 1 }}. {{
                question.question
              }}</p>
            <!-- 判断框 -->
            <div class="options"
                 style="justify-content: flex-end; margin-right:100px; display: flex; cursor: pointer;">
              <div v-for="(option, key) in { '√': 'true', '×': 'false' }"
                   :key="key"
                   style="flex: 0 0 10%; font-weight: normal; cursor: pointer;">
                <input type="radio" :id="`judge_option${index}${key}`" :name="`judge_question${index}`"
                       style=" cursor: pointer;"
                       @change="saveJudgeAnswer(index, option)"
                       :checked="option === question.user_answer">
                <label :for="`judge_option${index}${key}`" style="margin-left: 8px; cursor: pointer;">{{
                    key
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
        </div>
        <!-- 填空题 -->
        <div class="questions">
          <span class="question-title">三、填空题（每题 2 分）</span>
          <a-empty class="empty" v-if="questions.fillList.length <= 0"></a-empty>
          <div v-for="(question, index) in questions.fillList" :key="index">
            <!-- 题目 -->
            <p style="margin-left: 20px; margin-top: 15px; font-weight: normal;">{{ index + 1 }}. {{
                question.question
              }}</p>
            <!-- 输入框 -->
            <input class="input-box"
                   style="margin-left: 40px; width: 300px; height: 40px; font-size: 16px; padding: 7px;"
                   placeholder="请输入你的答案" @input="saveFillAnswer(index, $event)"
                   v-model="question.user_answer">
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
        </div>
        <!-- 计算题 -->
        <div class="questions">
          <span class="question-title">四、计算题（每题 2 分）</span>
          <a-empty class="empty" v-if="questions.calculateList.length <= 0"></a-empty>
          <div v-for="(question, index) in questions.calculateList" :key="index">
            <!-- 题目 -->
            <p style="margin-left: 20px; margin-top: 15px; font-weight: normal;">{{ index + 1 }}. {{
                question.question
              }}</p>
            <!-- 输入框 -->
            <input class="input-box"
                   style="margin-left: 40px; width: 800px; height: 40px; font-size: 16px; padding: 8px;"
                   placeholder="请输入" @input="saveCalculateAnswer(index, $event)"
                   v-model="question.user_answer">
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
        </div>
        <!-- 应用题 -->
        <div class="questions">
          <span class="question-title">五、应用题（每题 6 分）</span>
          <a-empty class="empty" v-if="questions.essayList.length <= 0"></a-empty>
          <div v-for="(question, index) in questions.essayList" :key="index">
            <!-- 题目 -->
            <p style="margin-left: 20px; margin-top: 15px; font-weight: normal;">{{ index + 1 }}. {{
                question.question
              }}</p>
            <!-- 输入框 -->
            <textarea class="input-box"
                      style="margin-left: 40px; width: 800px; height: 200px; font-size: 18px; padding: 10px;"
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
        </div>
        <!-- 得分和评价 -->
        <div
            style="margin-left: 30px; margin-top: 40px; font-size: 20px; font-weight: normal; font-family: '楷体', KaiTi, serif;"
            v-if="questions.comment">
          <p>得分：{{ questions.userScore }}</p>
          <p>总分：{{ questions.totalScore }}</p>
          <p>{{ questions.comment }}</p>
        </div>
        <!-- 底部按钮 -->
        <div style="display: flex; justify-content: flex-end; margin-top: 50px;">
          <a-popconfirm title="确定要提交吗?" ok-text="确定" cancel-text="取消"
                      @confirm="correct">
          <a-button class="generate-button" size="large" style="margin-right: 30px;"> 提交
          </a-button>
        </a-popconfirm>
          <a-popconfirm title="重做会清空之前的答题信息，确定要重做吗?" ok-text="确定" cancel-text="取消"
                        @confirm="reAnswer">
            <a-button class="generate-button" size="large" style="margin-right: 30px;"> 重答
            </a-button>
          </a-popconfirm>
          <a-button class="generate-button" size="large" @click="handleExit" style="margin-right: 30px;"> 退出
          </a-button>
        </div>
        <div class="space" style="height: 100px;"></div>
      </div>
      <!-- 回到顶部
      <div>
        <img :src="arrow" class="icon-arrow-up" alt="" @click="goToTop">
      </div>
      -->
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import {deleteRecordApi, getRecordApi} from "/@/api/record";
import {useUserStore} from "/@/store";
import {message} from "ant-design-vue";
import loading_img from "/@/assets/icons/loading.png";
import {ref} from "vue";
// import arrow from "/@/assets/icons/arrow-up-icon.png";
import {
  clearUserAnswerApi,
  getCalculateApi, getEssayApi, getFillApi, getJudgeApi, getMutiCalculateApi,
  getMutiEssayApi, getMutiFillApi, getMutiJudgeApi, getMutiSelectApi, getSelectApi,
  updateCalculateAnswerApi, updateEssayAnswerApi, updateFillAnswerApi, updateJudgeAnswerApi, updateSelectAnswerApi
} from "/@/api/questions";
import {
  getUserScoreApi, updateCalculateCommentApi, updateEssayCommentApi, updateFillCommentApi,
  updateJudgeCommentApi, updateSelectCommentApi, updateTotalScoreApi, updateUserScoreApi
} from "/@/api/correct";

const userStore = useUserStore();
const columns = reactive([
  {
    title: '序号',
    dataIdx: 'id',
    key: 'id',
    width: 60,
    align: 'center',
  },
  {
    title: '题目范围',
    dataIdx: 'question_range',
    key: 'question_range',
    align: 'center',
  },
  {
    title: '生成时间',
    dataIdx: 'generate_time',
    key: 'generate_time',
    align: 'center',
  },
  {
    title: '得分',
    dataIdx: 'user_score',
    key: 'user_score',
    align: 'center',
  },
  {
    title: '总分',
    dataIdx: 'total_score',
    key: 'total_score',
    align: 'center',
  },
  {
    title: '操作',
    dataIdx: 'operation',
    key: 'operation',
    align: 'center',
    fixed: 'right',
    width: 140,
  },
]);

// 页面数据
const data = reactive({
  recordList: [],                // 题目记录数据
  loading: false,                // 加载中
  keyword: '',
  selectedRowKeys: [] as any[],  // 选中的记录行
  pageSize: 6,                   // 每页最多展示的记录行
  page: 1,                       // 当前页码
});

// 题目弹窗
const modal = reactive({
  visible: false,
  title: '',
  index: '',
});

onMounted(() => {
  getRecordList();
});

const getRecordList = () => {
  data.loading = true;
  getRecordApi({username: userStore.user_name, keyword: data.keyword}).then((res) => {
    data.loading = false;
    console.log(res.data);
    res.data.forEach((item: any, id: any) => {
      item.id = id + 1;
    });
    data.recordList = res.data;
  }).catch((error) => {
    data.loading = false;
    console.log(error);
  });
}

const onSearchChange = (e: Event) => {
  // @ts-ignore
  data.keyword = e.target.value;
};

const onSearch = () => {
  getRecordList();
};

const rowSelection = ref({
  onChange: (selectedRowKeys: (string | number)[], selectedRows: any[]) => {
    data.selectedRowKeys = selectedRows.map((record) => record.index);
    console.log(`selectedRowKeys: ${data.selectedRowKeys}`, 'selectedRows: ', selectedRows);
  },
});


const handleBatchDelete = () => {
  if (data.selectedRowKeys.length <= 0) {
    message.warn('请勾选删除选项');
    return;
  }
  deleteRecordApi({username: userStore.user_name, ids: data.selectedRowKeys.join(',')}).then(() => {
    message.success('删除成功');
    data.selectedRowKeys = [];
    getRecordList();
  }).catch((error) => {
    message.warn(error.message || '操作失败');
  })
};

const confirmDelete = (record: any) => {
  deleteRecordApi({username: userStore.user_name, ids: record.id}).then(() => {
    getRecordList();
  }).catch((error) => {
    message.warn(error.message || '操作失败');
  })
}

const handleView = (question_range: any, index: any) => {
  // 出题次数和题目范围更新
  modal.visible = true;
  modal.title = question_range;
  modal.index = index;
  // 题目获取
  getQuestionsData();
};

const clearQuestionList = () => {
  for (let key in questions) {
    if (Array.isArray(questions[key])) {
      questions[key] = [];
    }
  }
};

const handleExit = () => {
  modal.visible = false;
  // 清空已获取的题目信息
  clearQuestionList();
};

const userAnswer = reactive({
  selectList: {},
  judgeList: {},
  fillList: {},
  calculateList: {},
  essayList: {},
});

// 用户答案保存
const saveSelectAnswer = (idx: any, option: string) => {
  userAnswer.selectList[idx + 1] = option;
  updateSelectAnswerApi({'username': userStore.user_name, 'index': modal.index, 'answer': userAnswer.selectList});
}
const saveJudgeAnswer = (idx: any, option: any) => {
  userAnswer.judgeList[idx + 1] = option;
  updateJudgeAnswerApi({'username': userStore.user_name, 'index': modal.index, 'answer': userAnswer.judgeList});
}
const saveFillAnswer = (idx: any, event: any) => {
  userAnswer.fillList[idx + 1] = event.target.value;
  updateFillAnswerApi({'username': userStore.user_name, 'index': modal.index, 'answer': userAnswer.fillList});
}
const saveCalculateAnswer = (idx: any, event: any) => {
  userAnswer.calculateList[idx + 1] = event.target.value;
  updateCalculateAnswerApi({'username': userStore.user_name, 'index': modal.index, 'answer': userAnswer.calculateList});
}
const saveEssayAnswer = (idx: any, event: any) => {
  userAnswer.essayList[idx + 1] = event.target.value;
  updateEssayAnswerApi({'username': userStore.user_name, 'index': modal.index, 'answer': userAnswer.essayList});
}

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

const getQuestionsData = () => {
  getMutiSelectApi({username: userStore.user_name, index: modal.index}).then((res) => {
    questions.selectList = questions.selectList.concat(res.data);
  });
  getMutiJudgeApi({username: userStore.user_name, index: modal.index}).then((res) => {
    questions.judgeList = questions.judgeList.concat(res.data);
  });
  getMutiFillApi({username: userStore.user_name, index: modal.index}).then((res) => {
    questions.fillList = questions.fillList.concat(res.data);
  });
  getMutiCalculateApi({username: userStore.user_name, index: modal.index}).then((res) => {
    questions.calculateList = questions.calculateList.concat(res.data);
  });
  getMutiEssayApi({username: userStore.user_name, index: modal.index}).then((res) => {
    questions.essayList = questions.essayList.concat(res.data);
  });
  getUserScoreApi({username: userStore.user_name, index: modal.index}).then((res) => {
    if (res.data) {
      questions.totalScore = res.data['total_score'];
      questions.userScore = res.data['user_score'];
      questions.comment = res.data['comment'];
    }
  });
};

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
  for (let i = 0; i < questions.selectList.length; i++) {
    questions.selectList[i].loading = true;
    await updateSelectCommentApi({
      'username': userStore.user_name,
      'index': modal.index,
      'question_idx': i
    }).then(() => {
      getSelectApi({username: userStore.user_name, index: modal.index, question_idx: i}).then((res) => {
        questions.selectList[i].flag = res.data['flag'];
        questions.selectList[i].comment = res.data['comment'];
        questions.selectList[i].loading = false;
      });
    });
  }
}

const updateJudgeComment = async () => {
  for (let i = 0; i < questions.judgeList.length; i++) {
    questions.judgeList[i].loading = true;
    await updateJudgeCommentApi({'username': userStore.user_name, 'index': modal.index, 'question_idx': i}).then(() => {
      getJudgeApi({username: userStore.user_name, index: modal.index, question_idx: i}).then((res) => {
        questions.judgeList[i].flag = res.data['flag'];
        questions.judgeList[i].comment = res.data['comment'];
        questions.judgeList[i].loading = false;
      });
    });
  }
}

const updateFillComment = async () => {
  for (let i = 0; i < questions.fillList.length; i++) {
    questions.fillList[i].loading = true;
    await updateFillCommentApi({'username': userStore.user_name, 'index': modal.index, 'question_idx': i}).then(() => {
      getFillApi({username: userStore.user_name, index: modal.index, question_idx: i}).then((res) => {
        questions.fillList[i].flag = res.data['flag'];
        questions.fillList[i].comment = res.data['comment'];
        questions.fillList[i].loading = false;
      });
    });
  }
}

const updateCalculateComment = async () => {
  for (let i = 0; i < questions.calculateList.length; i++) {
    questions.calculateList[i].loading = true;
    await updateCalculateCommentApi({
      'username': userStore.user_name,
      'index': modal.index,
      'question_idx': i
    }).then(() => {
      getCalculateApi({username: userStore.user_name, index: modal.index, question_idx: i}).then((res) => {
        questions.calculateList[i].flag = res.data['flag'];
        questions.calculateList[i].comment = res.data['comment'];
        questions.calculateList[i].loading = false;
      });
    });
  }
}

const updateEssayComment = async () => {
  for (let i = 0; i < questions.essayList.length; i++) {
    questions.essayList[i].loading = true;
    await updateEssayCommentApi({'username': userStore.user_name, 'index': modal.index, 'question_idx': i}).then(() => {
      getEssayApi({username: userStore.user_name, index: modal.index, question_idx: i}).then((res) => {
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
    await updateSelectComment();
    await updateJudgeComment();
    await updateFillComment();
    await updateCalculateComment();
    await updateEssayComment();
    // 打分
    await updateTotalScoreApi({'username': userStore.user_name, 'index': modal.index});  // 更新总分，防止出题中断导致总分为 0
    await updateUserScoreApi({'username': userStore.user_name, 'index': modal.index, 'flag': 'yes'});
    await getUserScoreApi({username: userStore.user_name, index: modal.index}).then((res) => {
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
  clearUserAnswerApi({'username': userStore.user_name, 'index': modal.index});
  location.reload();
}

const modalContent = ref<HTMLElement | null>(null);
const goToTop = () => {
  if (modalContent.value) {
    modalContent.value.scrollTo({
      top: 0,
      behavior: 'smooth' // 平滑滚动
    });
  }
};


</script>

<style scoped lang="less">
.page-view {
  background: #d9e2f6;
  padding: 24px;
  display: flex;
  flex-direction: column;
  font-family: '楷体', KaiTi, serif;
  font-size: 18px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;

  .page-title {
    font-size: 23px;
    font-weight: bold;
    color: #000C17FF;
    text-align: left;
  }

  .table-operations {
    display: flex;
    align-items: center;

    .deleteButton {
      background: #1E90FF;
      color: #ffffff;
      margin-left: auto;
      font-weight: bold;
      width: 100px;
    }

    .ant-input-search {
      margin-left: auto;
    }
  }
}

.table-operations > button {
  margin-right: 8px;
}

// 按钮
.generate-button {
  width: 100px;
  font-weight: bold;
  color: #ffffff;
  background: #1E90FF;
  font-family: '楷体', KaiTi, serif;
}

.icon-arrow-up {
  width: 45px;
  height: 45px;
  position: fixed;
  right: 100px;
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

// 题目样式设置
.modal {
  font-size: 18px;
  // max-height: 60vh;
  // overflow-y: auto;
}

.questions {
  margin-top: 40px;
  margin-left: 30px;
  font-family: '楷体', KaiTi, serif;

  .question-title {
    margin-top: 20px;
    font-weight: bold;
  }

  .empty {
    color: gray;
  }
}

.input-box {
  border: 1px solid gray;
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
  width: auto;
}

.question-comment {
  margin-left: 20px;
  font-weight: normal;
  color: #055081;
  margin-bottom: 20px;
}
</style>
