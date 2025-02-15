<template>
  <!-- 组件布局 -->
  <a-layout id="components-Layout" style="display: flex; flex-direction: column; height: 100vh;">
    <!-- 头部信息 -->
    <a-layout-header
        style="position: fixed; width: 100%; padding: 0; z-index: 1000; border-bottom: 1px solid gray; background: #d3dffa;">
      <div class="header">
        <img class="header-logo" :src="logo" alt="">
        <span class="header-title" style="color: #000c17">小学数学出题系统</span>
        <div class="empty"></div>
        <img class="default-avatar" :src="avatar" alt="" @click="changePersonal">
        <span style="font-weight: bold"> {{ userStore.user_name }} </span>
        <!-- 超链接进行页面跳转，回退到登录界面 -->
        <a class="header-quit" style="padding-right: 5px; padding-left: 5px" @click="handleLogout">退出</a>
      </div>
    </a-layout-header>

    <!-- 主体布局 -->
    <a-layout :style="{ marginTop: '64px' }">
      <!-- 侧边栏布局 -->
      <a-layout-sider collapsible :collapsed-width="60" :width="160"
                      style="position: fixed; height: calc(100vh - 64px); overflow-y: auto; z-index: 999;"
                      @collapse="handleCollapse" @expand="handleExpand">
        <a-menu
            style="overflow:auto; overflow-x: hidden;"
            v-model:selectedKeys="selectedKeys" theme="dark"
            mode="inline" @click="handleClick">
          <!-- 单元测试 -->
          <a-menu-item key="unitTest">
            <img class="sider-logo" :src="unit" alt="">
            <span class="sider-title">单元测试</span>
          </a-menu-item>
          <!-- 综合测试 -->
          <a-menu-item key="integratedTest">
            <img class="sider-logo" :src="integrated" alt="">
            <span class="sider-title">综合测试</span>
          </a-menu-item>
          <!-- 题库管理 -->
          <a-menu-item key="questionBank">
            <img class="sider-logo" :src="question" alt="">
            <span class="sider-title">题库管理</span>
          </a-menu-item>
          <!-- 个人中心 -->
          <a-menu-item key="personalCenter">
            <img class="sider-logo" :src="personal" alt="">
            <span class="sider-title">个人中心</span>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>

      <!-- 内容布局 -->
      <a-layout-content
          :style="{
          paddingLeft: collapsed ? '60px' : '160px',
          marginTop: '0',
          minHeight: 'calc(100vh - 64px)',
          overflowY: 'auto',
        }">
        <router-view/>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>
<script setup lang="ts">
import {useRouter, useRoute} from 'vue-router'

import logo from '/@/assets/icons/math-icon.png'
import avatar from '/@/assets/icons/avatar.png'
import unit from '/@/assets/icons/unit.png'
import integrated from '/@/assets/icons/integrated.png'
import question from '/@/assets/icons/question.png'
import personal from '/@/assets/icons/personal.png'

import {ref} from 'vue';
import {useUserStore} from "/@/store";

const userStore = useUserStore();

const selectedKeys = ref<any[]>([])
const collapsed = ref(false);
const handleCollapse = (collapsedState: boolean) => {
  collapsed.value = collapsedState;
};

const handleExpand = () => {
  collapsed.value = false;
};

const router = useRouter()
const route = useRoute()

// 侧边栏点击
const handleClick = ({key}) => {
  console.log('点击路由===>', key)
  router.push({
    name: key,
  })
}

// 侧边栏选中
onMounted(() => {
  console.log('当前路由===>', route.name)
  selectedKeys.value = [route.name]
})

// 点击头像进入个人中心
const changePersonal = () => {
  router.push({name: 'personalCenter'});
  selectedKeys.value = ['personalCenter'];
}

// 退出登录
const handleLogout = () => {
  userStore.adminLogout().then(() => {
    router.push({name: 'adminLogin'})
  })
}

</script>
<style scoped lang="less">

// header样式
.header {
  display: flex;
  flex-direction: row;
  align-items: center; // 垂直居中
  padding-left: 24px;
  padding-right: 24px;

  .header-logo {
    width: 33px;
    height: 33px;
    cursor: pointer;
  }

  .header-title {
    margin-left: 20px;
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    font-family: '楷体', KaiTi, serif;
  }

  .empty {
    flex: 1;
  }

  .header-quit {
    margin-left: 12px;
  }
}

// 头像
.default-avatar {
  width: 30px;
  height: 30px;
  margin-right: 10px;
  cursor: pointer;
  transition: transform 0.3s;
}

.default-avatar:hover {
  transform: scale(1.1);
}

.default-avatar:active {
  transform: scale(0.9);
}

.sider-logo {
  width: 20px;
  height: 20px;
  margin-right: 20px;
  margin-bottom: 4px;
}

#components-Layout .trigger {
  font-size: 18px;
  line-height: 64px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-Layout .trigger:hover {
  color: #1890ff;
}

:deep(.ant-layout-content) {
  overflow-x: hidden;
  overflow-y: auto;
}

:deep(.ant-menu) {
  padding-top: 10px;
}

</style>
