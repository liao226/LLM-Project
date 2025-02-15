<template>
  <div class="page-view">
    <!-- 账号信息 -->
    <span class="page-title">账号信息</span>
    <hr style="border-top: 1px solid #cdcdcd; margin-top: 5px;">
    <!-- 头像和点击后出现的信息 -->
    <div style="display: flex; align-items: center;">
      <!-- 头像 -->
      <img class="default-avatar" :src="avatar" alt="" @click="clickAvatar">
      <!-- 头像右边的文字 -->
      <span style="margin-left: 30px; font-size: 18px; color: #055081;" v-if="avatarMessage">{{ avatarMessage }}</span>
    </div>
    <!-- 账号和密码 -->
    <div class="username" style="display: flex; align-items: flex-end; flex-wrap: wrap;">
      <span class="title">账号名：</span>
      <span class="content">{{ userStore.user_name }}</span>
      <a class="edit" @click="changeUsername">修改</a>
    </div>
    <div class="password" style="border-bottom: 1px solid gray; padding-bottom: 20px;">
      <a @click="changePwd">修改密码</a>
      <a-popconfirm title="注销账户会删除所有信息，确定要注销吗?" ok-text="确定" cancel-text="取消"
                    @confirm="deleteUser">
        <a href="#" style="margin-left: 60px;">注销账户</a>
      </a-popconfirm>
    </div>

    <!-- 题目设置 -->
    <span class="page-title" style="margin-top: 30px;">题型设置</span>
    <hr style="border-top: 1px solid #cdcdcd; margin-top: 5px;">
    <!-- 题型数量设置 -->
    <div class="checkbox-container" style="border-bottom: 1px solid gray; padding-bottom: 20px;">
      <!-- 选择题 -->
      <div class="checkbox-row">
        <input type="checkbox" id="multiple-choice" class="select-box" v-model="isSelectSelected">
        <label for="multiple-choice">选择题</label>
        <div class="quantity-input">
          <button class="quantity-btn" id="decrease" @click="de_select">-</button>
          <input type="number" id="select-quantity" min="0" v-model="select_quantity" checked>
          <button class="quantity-btn" id="increase" @click="in_select">+</button>
        </div>
      </div>
      <!-- 判断题 -->
      <div class="checkbox-row">
        <input type="checkbox" id="judge" class="select-box" v-model="isJudgeSelected">
        <label for="judge">判断题</label>
        <div class="quantity-input">
          <button class="quantity-btn" id="decrease" @click="de_judge">-</button>
          <input type="number" id="judge-quantity" min="0" v-model="judge_quantity" checked>
          <button class="quantity-btn" id="increase" @click="in_judge">+</button>
        </div>
      </div>
      <!-- 填空题 -->
      <div class="checkbox-row">
        <input type="checkbox" id="fill-blank" class="select-box" v-model="isFillSelected">
        <label for="fill-blank">填空题</label>
        <div class="quantity-input">
          <button class="quantity-btn" id="decrease" @click="de_fill">-</button>
          <input type="number" id="fill-quantity" min="0" v-model="fill_quantity" checked>
          <button class="quantity-btn" id="increase" @click="in_fill">+</button>
        </div>
      </div>
      <!-- 计算题 -->
      <div class="checkbox-row">
        <input type="checkbox" id="calculation" class="select-box" v-model="isCalculateSelected">
        <label for="calculation">计算题</label>
        <div class="quantity-input">
          <button class="quantity-btn" id="decrease" @click="de_calculate">-</button>
          <input type="number" id="calculate-quantity" min="0" v-model="calculate_quantity" checked>
          <button class="quantity-btn" id="increase" @click="in_calculate">+</button>
        </div>
      </div>
      <!-- 问答题 -->
      <div class="checkbox-row">
        <input type="checkbox" id="essay" class="select-box" v-model="isEssaySelected">
        <label for="essay">问答题</label>
        <div class="quantity-input">
          <button class="quantity-btn" id="decrease" @click="de_essay">-</button>
          <input type="number" id="essay-quantity" min="0" v-model="essay_quantity" checked>
          <button class="quantity-btn" id="increase" @click="in_essay">+</button>
        </div>
        <a-button size="large" @click="resetSetting"
                  style="margin-left: 50px; width: 127px; font-weight: bold; color: #ffffff; background: #1E90FF;">
          恢复初始设置
        </a-button>
      </div>
    </div>

    <!-- 系统介绍 -->
    <span class="page-title" style="margin-top: 30px;">系统介绍</span>
    <hr style="border-top: 1px solid #cdcdcd; margin-top: 5px;">
    <p style="text-align: justify; text-indent: 2em; margin-top: 20px; font-size: 18px;">
      本系统为小学数学出题系统，题库知识点主要来源于人教版小学数学教材。<br>
    </p>
    <p style="text-align: justify; text-indent: 2em; font-size: 18px;">
      【单元测试】：用户可以选择年级和单元，点击“生成”按钮或“留在本阶段”按钮，系统将生成有关的题目。用户在回答结束后，点击页面右下角的“提交”按钮，系统将根据用户答案进行批改，用户可以在每道题目下方看到批改结果和该题的解析，并在所有题目最后看到自己的得分和评语。如果对上次做答结果不满意，可以通过点击“重做”按钮重新做答。如果发现系统出的题目有误，可以点击“错题反馈”进行反馈，系统将自动删除表达错误或不清晰的题目。通过点击“进入下一阶段”，系统将自动调整进度为下一单元，并进行出题。
    </p>
    <p style="text-align: justify; text-indent: 2em; font-size: 18px;">
      【综合测试】：用户可以选择年级，点击“生成”按钮，系统将随机抽取各个单元的知识点生成有关的题目。其余功能与【单元测试】一致。
    </p>
    <p style="text-align: justify; text-indent: 2em; font-size: 18px;">
      【题库管理】：用户的出题记录将按照生成时间降序排列，记录中的得分为用户最近一次提交的得分。用户可以查看或删除有关的题目记录，也可以在查看时选择重新做答。
    </p>
    <p style="text-align: justify; text-indent: 2em; font-size: 18px;">
      【个人中心】：用户可以在该页面修改个人账号信息和题型设置信息，点击“恢复初始设置”按钮可以将题型设置恢复到更改前的默认设置，系统将根据用户的题型设置信息进行出题。
    </p>
    <p style="text-align: justify; text-indent: 2em; font-size: 18px; color: #ef4848;">
      【注意】：系统在出题或判题时切换页面，或执行答题外的其它操作，可能导致出题页面正在执行的任务被打断，此时重新出题或提交，任务将重头开始。
    </p>
    <!-- 空白区域 -->
    <div class="space" style="height: 200px;"></div>

    <!-- 弹窗区域 -->
    <div>
      <a-modal
          :visible="modal.visible"
          :forceRender="true"
          :title="modal.title"
          ok-text="确认"
          cancel-text="取消"
          @cancel="handleCancel"
          @ok="handleOk"
      >
        <div>
          <a-form ref="modalform" :label-col="{ style: { width: '80px' } }" :model="modal.form" :rules="modal.rules">
            <a-row :gutter="24">
              <!-- 账户名 -->
              <a-col span="23" v-if="modal.updateName">
                <a-form-item label="账户名" name="new_username">
                  <a-input style="font-family: '楷体', KaiTi, serif" placeholder="请输入新账户名"
                           v-model:value="modal.form.new_username" allowClear/>
                </a-form-item>
              </a-col>
              <!-- 密码 -->
              <a-col span="23" v-if="!modal.updateName">
                <a-form-item label="新密码" name="password">
                  <a-input style="font-family: '楷体', KaiTi, serif" placeholder="请输入新密码" type="password"
                           v-model:value="modal.form.password" allowClear/>
                </a-form-item>
              </a-col>
              <!-- 确认密码 -->
              <a-col span="23" v-if="!modal.updateName">
                <a-form-item label="确认密码" name="second_password">
                  <a-input style="font-family: '楷体', KaiTi, serif" placeholder="请再次输入密码" type="password"
                           v-model:value="modal.form.second_password" allowClear/>
                </a-form-item>
              </a-col>
            </a-row>
          </a-form>
        </div>
      </a-modal>
    </div>
  </div>
</template>

<script setup lang="ts">
import avatar from '/@/assets/icons/avatar.png'

import {useUserStore} from "/@/store";
import {message} from "ant-design-vue";
import {clickAvatarApi, deleteUserApi, updatePwdApi, updateUsernameApi} from "/@/api/user";
import {useRouter} from 'vue-router'
import {getSettingApi, resetSettingApi, updateFlagApi, updateQuantityApi} from "/@/api/setting";

const userStore = useUserStore();

// 题型选择
const isSelectSelected = ref();
const isJudgeSelected = ref();
const isFillSelected = ref();
const isCalculateSelected = ref();
const isEssaySelected = ref();
watch([isSelectSelected, isJudgeSelected, isFillSelected, isCalculateSelected, isEssaySelected], () => {
  updateFlagApi({
    'username': userStore.user_name,
    'select_flag': String(isSelectSelected.value),
    'judge_flag': String(isJudgeSelected.value),
    'fill_flag': String(isFillSelected.value),
    'calculate_flag': String(isCalculateSelected.value),
    'essay_flag': String(isEssaySelected.value)
  }).then(() => {
  }).catch((err) => {
    console.log(err);
    message.warn(err.message || "题型更新失败")
  });
});

// 选择题数量
const select_quantity = ref();
watch(select_quantity, (newValue) => {
  updateQuantityApi({
    'username': userStore.user_name,
    'type': 'select_quantity',
    'select_quantity': newValue
  }).then(() => {
  }).catch((err) => {
    console.log(err);
    message.warn(err.message || "题型更新失败")
  });
});
const de_select = () => {
  const cut = parseInt(select_quantity.value);
  select_quantity.value = Math.max(cut - 1, 0).toString();
}
const in_select = () => {
  const cut = parseInt(select_quantity.value);
  select_quantity.value = Math.min(cut + 1, 100).toString();
}

// 判断题数量
const judge_quantity = ref();
watch(judge_quantity, (newValue) => {
  updateQuantityApi({
    'username': userStore.user_name,
    'type': 'judge_quantity',
    'judge_quantity': newValue
  }).then(() => {
  }).catch((err) => {
    console.log(err);
    message.warn(err.message || "题型更新失败")
  });
});
const de_judge = () => {
  const cut = parseInt(judge_quantity.value);
  judge_quantity.value = Math.max(cut - 1, 0).toString();
}
const in_judge = () => {
  const cut = parseInt(judge_quantity.value);
  judge_quantity.value = Math.min(cut + 1, 100).toString();
}

// 填空题
const fill_quantity = ref();
watch(fill_quantity, (newValue) => {
  updateQuantityApi({
    'username': userStore.user_name,
    'type': 'fill_quantity',
    'fill_quantity': newValue
  }).then(() => {
  }).catch((err) => {
    console.log(err);
    message.warn(err.message || "题型更新失败")
  });
});
const de_fill = () => {
  const cut = parseInt(fill_quantity.value);
  fill_quantity.value = Math.max(cut - 1, 0).toString();
}
const in_fill = () => {
  const cut = parseInt(fill_quantity.value);
  fill_quantity.value = Math.min(cut + 1, 100).toString();
}

// 计算题
const calculate_quantity = ref();
watch(calculate_quantity, (newValue) => {
  updateQuantityApi({
    'username': userStore.user_name,
    'type': 'calculate_quantity',
    'calculate_quantity': newValue
  }).then(() => {
  }).catch((err) => {
    console.log(err);
    message.warn(err.message || "题型更新失败")
  });
});
const de_calculate = () => {
  const cut = parseInt(calculate_quantity.value);
  calculate_quantity.value = Math.max(cut - 1, 0).toString();
}
const in_calculate = () => {
  const cut = parseInt(calculate_quantity.value);
  calculate_quantity.value = Math.min(cut + 1, 100).toString();
}

// 应用题
const essay_quantity = ref();
watch(essay_quantity, (newValue) => {
  updateQuantityApi({
    'username': userStore.user_name,
    'type': 'essay_quantity',
    'essay_quantity': newValue
  }).then(() => {
  }).catch((err) => {
    console.log(err);
    message.warn(err.message || "题型更新失败")
  });
});
const de_essay = () => {
  const cut = parseInt(essay_quantity.value);
  essay_quantity.value = Math.max(cut - 1, 0).toString();
}
const in_essay = () => {
  const cut = parseInt(essay_quantity.value);
  essay_quantity.value = Math.min(cut + 1, 100).toString();
}

// 加载用户题型设置
const getSetting = () => {
  getSettingApi({
    username: userStore.user_name,
  }).then((res) => {
    console.log(res.data);
    // 题型选择
    isSelectSelected.value = res.data['select_flag'];
    isJudgeSelected.value = res.data['judge_flag'];
    isFillSelected.value = res.data['fill_flag'];
    isCalculateSelected.value = res.data['calculate_flag'];
    isEssaySelected.value = res.data['essay_flag'];
    // 数量设置
    select_quantity.value = res.data['select_quantity'];
    judge_quantity.value = res.data['judge_quantity'];
    fill_quantity.value = res.data['fill_quantity'];
    calculate_quantity.value = res.data['calculate_quantity'];
    essay_quantity.value = res.data['essay_quantity'];
  }).catch((error) => {
    console.log(error);
  });
};

const resetSetting = () => {
  resetSettingApi({'username': userStore.user_name}).then(() => {
    location.reload();  // 刷新页面重新加载题型设置信息
    message.success('题型设置重置成功！');
  });
}

onMounted(() => {
  getSetting();
  avatarMessage.value = '';
});

// 点击头像
const avatarMessage = ref('');
const clickAvatar = () => {
  clickAvatarApi({}).then((res) => {
    avatarMessage.value = res.data['message'];
  });
}

// 弹窗数据
const modalform = ref();
const modal = reactive({
  visible: false,
  updateName: false,
  title: "",
  // 账号和密码
  form: {
    id: undefined,
    username: userStore.user_name,
    new_username: undefined,
    password: undefined,
    second_password: undefined,
  },
  rules: {
    new_username: [{required: true, message: '请输入', trigger: 'blur'}],
    password: [{required: true, message: '请输入', trigger: 'blur'}],
    second_password: [{required: true, message: '请输入', trigger: 'blur'}],
  },
})
// 修改账号名
const changeUsername = () => {
  resetModal();
  modal.visible = true;
  modal.updateName = true;
  modal.title = "修改账号名";
  // 重置表单
  for (const key in modal.form) {
    modal.form[key] = undefined;
  }
}

// 修改密码
const changePwd = () => {
  resetModal();
  modal.visible = true;
  modal.updateName = false;
  modal.title = "修改密码";
  // 重置表单
  for (const key in modal.form) {
    modal.form[key] = undefined;
  }
}
const handleOk = () => {
  modalform.value?.validate().then(() => {
    const formData = new FormData();
    formData.append('username', userStore.user_name);
    if (modal.form.new_username) {
      formData.append('new_username', modal.form.new_username);
    }
    if (modal.form.password) {
      formData.append('password', modal.form.password);
    }
    if (modal.form.second_password) {
      if (modal.form.second_password !== modal.form.password) {
        message.error('两次密码输入不一致，请重新输入!');
        modal.form.second_password = undefined;
      }
    }

    // 更新账户名
    if (modal.updateName && modal.form.new_username) {
      localStorage.setItem('user_name', modal.form.new_username);
      updateUsernameApi(formData).then(() => {
        hideModal();
        message.success('账户名修改成功！');
        location.reload();
      }).catch((err) => {
        console.log(err);
        message.warn(err.message || "账户名修改失败")
      });
    }
    // 更新密码
    else if (!modal.updateName && modal.form.password && modal.form.second_password) {
      // 更新用户数据库
      updatePwdApi(formData).then(() => {
        hideModal();
        message.success('密码修改成功！');
      }).catch((err) => {
        console.log(err);
        message.warn(err.message || "密码修改失败")
      });
    }
  }).catch(() => {
    message.error('输入不能为空！');
  })
}
const handleCancel = () => {
  hideModal();
};

// 恢复注册弹窗表单初始状态
const resetModal = () => {
  modalform.value?.resetFields();
};

// 隐藏弹窗
const hideModal = () => {
  modal.visible = false;
}

// 注销账户
const router = useRouter()
const deleteUser = () => {
  const formData = new FormData();
  formData.append('username', userStore.user_name);
  deleteUserApi(formData).then(() => {
    userStore.adminLogout().then(() => {
      router.push({name: 'adminLogin'})
    })
    message.success('注销成功！');
  }).catch(() => {
    message.error('注销失败！');
  })
}

</script>

<style scoped lang="less">

.page-view {
  min-height: 100%;
  font-family: '楷体', KaiTi, serif;
  padding: 24px;
  display: flex;
  flex-direction: column;
  background: #d9e2f6;
}

.page-title {
  font-family: '楷体', KaiTi, serif;
  font-size: 23px;
  font-weight: bold;
  color: #000C17FF;
}

// 头像显示
.default-avatar {
  width: 55px;
  height: 55px;
  margin-top: 20px;
  margin-left: 20px;
  margin-bottom: 20px;
  border: 1.5px solid #52565b;
  border-radius: 15%;
  padding: 10px;
  cursor: pointer;
  transition: transform 0.3s;
}

.default-avatar:active {
  transform: scale(0.95);
}

// 用户名设置
.username {
  font-size: 18px;
  color: #113354;

  .title {
    margin-right: 10px;
  }

  // 用户名显示
  .content {
    margin-right: 5px;
    border: 1.5px solid #52565b;
    border-radius: 5px;
    width: 250px;
    padding: 5px 5px 5px 10px;
  }

  // 修改用户名
  .edit {
    font-size: 15px;
  }
}

// 修改密码
.password {
  font-size: 18px;
  margin-top: 25px;
}

// 题型设置
.checkbox-container {
  margin-top: 20px;
  font-size: 18px;

  .checkbox-row {
    display: flex;
    align-items: center;
    margin-bottom: 10px;

    // 复选框
    .select-box {
      margin-right: 10px;
    }

    .quantity-input {
      margin-left: 80px;
      display: flex;
      align-items: center;
    }

    .quantity-input input[type="number"] {
      border-radius: 5px;
      padding: 2px 2px 2px 8px;
    }

    // 数量加减按钮
    .quantity-btn {
      margin: 0 7px; // 加减按钮之间的间距
      width: 30px;
      height: 30px;
    }
  }
}

</style>
