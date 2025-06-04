<script setup lang="ts">
import { ref, computed } from 'vue'
import ClientStatus from './components/ClientStatus.vue'
import AccountStatus from './components/AccountStatus.vue'
import CallStatus from './components/CallStatus.vue'

const activeTab = ref('account')

const currentComponent = computed(() => {
  switch (activeTab.value) {
    case 'account':
      return AccountStatus
    case 'client':
      return ClientStatus
    case 'call':
      return CallStatus
    default:
      return ClientStatus
  }
})

const getCurrentPageTitle = computed(() => {
  switch (activeTab.value) {
    case 'account':
      return '账号状态'
    case 'client':
      return '客户端状态'
    case 'call':
      return '通话状态'
    default:
      return ''
  }
})
</script>

<template>
  <div class="app-container">
    <!-- 侧边栏 -->
    <div class="sidebar">
      <div class="logo">
        <el-icon class="logo-icon">
          <Monitor />
        </el-icon>
        <span>管理系统</span>
      </div>
      <el-menu :default-active="activeTab" class="sidebar-menu" background-color="#001529" text-color="#fff"
        active-text-color="#409EFF">
        <el-menu-item index="account" @click="activeTab = 'account'">
          <el-icon>
            <User />
          </el-icon>
          <span>账号状态</span>
        </el-menu-item>
        <el-menu-item index="client" @click="activeTab = 'client'">
          <el-icon>
            <Monitor />
          </el-icon>
          <span>客户端状态</span>
        </el-menu-item>
        <el-menu-item index="call" @click="activeTab = 'call'">
          <el-icon>
            <Phone />
          </el-icon>
          <span>通话状态</span>
        </el-menu-item>
      </el-menu>
    </div>

    <!-- 主内容区 -->
    <div class="main-content">
      <div class="header">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>首页</el-breadcrumb-item>
          <el-breadcrumb-item>{{ getCurrentPageTitle }}</el-breadcrumb-item>
        </el-breadcrumb>
        <!-- <div class="user-info">
          <el-dropdown>
            <span class="user-dropdown">
              管理员 <el-icon><ArrowDown /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>个人信息</el-dropdown-item>
                <el-dropdown-item>退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
</el-dropdown>
</div> -->
      </div>

      <div class="content">
        <component :is="currentComponent" />
      </div>
    </div>
  </div>
</template>

<style>
html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

#app {
  height: 100%;
  width: 100%;
}

.app-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  background-color: #f0f2f5;
}

.sidebar {
  width: 240px;
  background-color: #001529;
  height: 100%;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
}

.logo {
  height: 64px;
  display: flex;
  align-items: center;
  padding: 0 24px;
  color: #fff;
  font-size: 18px;
  font-weight: bold;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.logo-icon {
  margin-right: 12px;
  font-size: 24px;
}

.sidebar-menu {
  flex: 1;
  border-right: none;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
  height: 100%;
}

.header {
  height: 64px;
  background-color: #fff;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  flex-shrink: 0;
}

.user-info {
  display: flex;
  align-items: center;
}

.user-dropdown {
  display: flex;
  align-items: center;
  cursor: pointer;
  color: #666;
}

.user-dropdown .el-icon {
  margin-left: 8px;
}

.content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  min-height: 0;
}

:deep(.el-menu-item) {
  display: flex;
  align-items: center;
}

:deep(.el-menu-item .el-icon) {
  margin-right: 12px;
  font-size: 18px;
}

:deep(.el-breadcrumb) {
  font-size: 14px;
}

:deep(.el-dropdown-menu__item) {
  font-size: 14px;
}
</style>
