<template>
  <!-- 用户界面布局 -->
  <div id="userLayout">
    <!-- 头部信息，包括 logo 和标题 -->
    <div class="user-layout-header">
      <img class="logo" :src="logoImage" alt="">
      <span>小学数学出题系统</span>
    </div>
    <!-- 登录 -->
    <div class="main-container">
      <div class="main">
        <div class="main-right">
          <!-- 表单 -->
          <a-form
              ref="myform"
              layout="vertical"
              :model="data.loginForm"
              :rules="data.rules"
              :hideRequiredMark="true"
          >
            <!-- 账号 -->
            <a-form-item name="username" label="账号" :colon="false">
              <a-input
                  size="large"
                  placeholder="请输入登录账号"
                  style="font-family: '楷体', KaiTi, serif; background: #f0f0f0"
                  v-model:value="data.loginForm.username"
                  @pressEnter="handleSubmit">
              </a-input>
            </a-form-item>
            <!-- 密码 -->
            <a-form-item name="password" label="密码" :colon="false">
              <a-input
                  size="large"
                  type="password"
                  placeholder="请输入登录密码"
                  style="font-family: '楷体', KaiTi, serif; background: #f0f0f0"
                  v-model:value="data.loginForm.password"
                  @pressEnter="handleSubmit">
              </a-input>
            </a-form-item>
            <!-- 登录和注册按钮 -->
            <div class="button-container">
              <!-- 登录按钮 -->
              <a-form-item>
                <a-button
                    class="login-button"
                    type="primary"
                    :loading="loginBtn"
                    block
                    size="large"
                    @click="handleSubmit"
                >
                  登录
                </a-button>
              </a-form-item>
              <!-- 注册按钮 -->
              <a-form-item>
                <a-button
                    class="register-button"
                    type="primary"
                    :loading="registerBtn"
                    block
                    size="large"
                    @click="handleRegister"
                >
                  注册
                </a-button>
              </a-form-item>
            </div>
          </a-form>
          <!-- 错误提示 -->
          <div class="error-tip"></div>
          <!-- 忘记密码 -->
          <a @click="forgetPwd"> 忘记密码？</a>
        </div>
      </div>
    </div>

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
              <!-- 账号 -->
              <a-col span="23">
                <a-form-item label="账号" name="username">
                  <a-input style="font-family: '楷体', KaiTi, serif" placeholder="请输入账号"
                           v-model:value="modal.form.username" allowClear/>
                </a-form-item>
              </a-col>
              <!-- 密码 -->
              <a-col span="23">
                <a-form-item :label="modal.updatePwd ? '新密码' : '密码'" name="password">
                  <a-input style="font-family: '楷体', KaiTi, serif" placeholder="请输入密码" type="password"
                           v-model:value="modal.form.password" allowClear/>
                </a-form-item>
              </a-col>
              <!-- 确认密码 -->
              <a-col span="23">
                <a-form-item label="确认密码" name="second_password">
                  <a-input style="font-family: '楷体', KaiTi, serif" placeholder="请输入密码" type="password"
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
import {useUserStore} from '/@/store';
import logoImage from '/@/assets/icons/math-icon.png';

const router = useRouter();
const userStore = useUserStore();

import {message} from "ant-design-vue";
import {addApi, updatePwdApi} from "/@/api/user";

const myform = ref()
const modalform = ref()

const loginBtn = ref<Boolean>(false)
const registerBtn = ref<Boolean>(false)
const checked = ref<Boolean>(false)

// 登录数据
const data = reactive({
  loginForm: {
    username: '',
    password: '',
  },
  rules: {
    username: [{required: true, message: '请输入账号', trigger: 'blur'}],
    password: [{required: true, message: '请输入密码', trigger: 'blur'}]
  }
})

// 处理登录
const handleSubmit = () => {
  myform.value?.validate().then(() => {
    handleLogin()
  }).catch(() => {
    message.error('账号和密码均不能为空！')
  })
}

const handleLogin = () => {
  userStore.adminLogin({
    username: data.loginForm.username,
    password: data.loginForm.password,
  }).then(() => {
    loginSuccess()
  }).catch(err => {
    message.error(err.message || '账号或密码错误!')
  })
}

const loginSuccess = () => {
  router.push({path: '/admin'})
  message.success('登录成功！')
}

// 弹窗数据
const modal = reactive({
  visible: false,
  updatePwd: false,
  title: "",
  // 账号和密码
  form: {
    id: undefined,
    username: undefined,
    password: undefined,
    second_password: undefined,
  },
  rules: {
    username: [{required: true, message: '请输入账号', trigger: 'blur'}],
    password: [{required: true, message: '请输入密码', trigger: 'blur'}],
    second_password: [{required: true, message: '再次确认密码', trigger: 'blur'}],
  },
})

const forgetPwd = () => {
  resetModal();
  modal.visible = true;
  modal.updatePwd = true;
  modal.title = "修改密码";
  // 重置表单
  for (const key in modal.form) {
    modal.form[key] = undefined;
  }
}

const handleRegister = () => {
  resetModal();
  modal.visible = true;
  modal.updatePwd = false;
  modal.title = "注册";
  // 重置表单
  for (const key in modal.form) {
    modal.form[key] = undefined;
  }
}

const handleOk = () => {
  modalform.value?.validate().then(() => {
    const formData = new FormData();
    if (modal.form.username) {
      formData.append('username', modal.form.username);
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

    // 添加用户数据
    if (!modal.updatePwd && modal.form.username && modal.form.password && modal.form.second_password) {
      // 更新用户数据库
      addApi(formData).then(() => {
        hideModal();
        message.success('注册成功！');
      }).catch((err) => {
        console.log(err);
        message.warn(err.message || "注册失败")
      });
    }
    // 更新密码
    else if (modal.updatePwd && modal.form.username && modal.form.password && modal.form.second_password) {
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
    message.error('账号和密码均不能为空！');
  })
}

// 取消注册
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

</script>

<style lang="less" scoped>

#userLayout {
  position: relative;
  height: 100vh;

  // 背景图
  background-image: url('/src/assets/images/login-bg.jpg');
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;

  .user-layout-header {
    height: 80px;
    padding: 0 24px;
    font-family: '楷体', KaiTi, serif;
    color: fade(#ffffff, 85%);
    font-size: 28px;
    font-weight: bold;
    line-height: 80px;

    .logo {
      width: 36px;
      height: 36px;
      margin-right: 10px;
      margin-top: -4px;
    }
  }

  .main-container {
    width: 100%;
    height: calc(100vh - 80px);

    .main {
      position: absolute;
      right: 80px;
      top: 50%;
      display: flex;
      transform: translate(0, -50%);
      border-radius: 8px;
      overflow: hidden;

      .main-right {
        background: #f0f0f0;
        padding: 24px;
        width: 420px;
        user-select: none;

        .sys_title {
          font-size: 24px;
          color: fade(#000, 85%);
          font-weight: bold;
          user-select: none;
          padding-bottom: 8px;
        }

        :deep(.ant-form-item label) {
          font-weight: bold;
        }

        .flex {
          align-items: center;
          display: flex;
          justify-content: space-between;
        }

        .forget_password {
          cursor: pointer;
        }

        .button-container {
          display: grid;
          grid-template-columns: auto auto;
          padding-top: 23px;
          gap: 10px;

          .login-button {
            background: linear-gradient(128deg, #00aaeb, #00c1cd 59%, #0ac2b0 100%);
          }

          .register-button {
            background: linear-gradient(128deg, #00aaeb, #00c1cd 59%, #0ac2b0 100%);
          }
        }
      }

      .error-tip {
        text-align: center;
      }
    }
  }
}
</style>
