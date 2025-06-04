<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { accountApi } from '../api'
import { ElMessage } from 'element-plus'
import type { Account } from '../types/Account'
import '../assets/style.css'

const accounts = ref<Account[]>([])
const newAccount = ref<{ name: string; pwd: string; host: string }>({ name: '', pwd: '', host: '' })
const dialogVisible = ref(false)
const editingAccount = ref<Account | null>(null)

// 获取账号列表
const fetchAccounts = async () => {
  try {
    const response = await accountApi.getAccounts()
    accounts.value = response.data
  } catch (error: any) {
    ElMessage.error(error.message || '获取账号列表失败')
  }
}

// 添加或更新账号
const addAccount = async () => {
  try {
    if (editingAccount.value) {
      // 编辑账号
      await accountApi.updateAccount(editingAccount.value.id, newAccount.value)
      ElMessage.success('更新账号成功')
    } else {
      // 添加账号
      await accountApi.addAccount(newAccount.value)
      ElMessage.success('添加账号成功')
    }
    dialogVisible.value = false
    newAccount.value = { name: '', pwd: '', host: '' }
    editingAccount.value = null
    fetchAccounts()
  } catch (error: any) {
    ElMessage.error(error.message || (editingAccount.value ? '更新账号失败' : '添加账号失败'))
  }
}

// 编辑账号
const editAccount = (account: Account) => {
  editingAccount.value = account
  newAccount.value = { name: account.name, pwd: account.pwd, host: account.host }
  dialogVisible.value = true
}

// 删除账号
const deleteAccount = async (id: number) => {
  try {
    await accountApi.deleteAccount(id)
    ElMessage.success('删除账号成功')
    fetchAccounts()
  } catch (error: any) {
    ElMessage.error(error.message || '删除账号失败')
  }
}

// 打开添加对话框
const openAddDialog = () => {
  editingAccount.value = null
  newAccount.value = { name: '', pwd: '', host: '' }
  dialogVisible.value = true
}

onMounted(() => {
  fetchAccounts()
})
</script>

<template>
  <div class="account-status">
    <!-- 统计卡片 -->
    <div class="stat-cards">
      <el-row :gutter="20">
        <el-col :span="8">
          <el-card class="stat-card">
            <template #header>
              <div class="card-header">
                <span>总账号数</span>
                <el-tag type="info">总数</el-tag>
              </div>
            </template>
            <div class="card-content">
              <div class="number">{{ accounts.length }}</div>
              <div class="text">个账号</div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card class="stat-card">
            <template #header>
              <div class="card-header">
                <span>已注册账号</span>
                <el-tag type="success">活跃</el-tag>
              </div>
            </template>
            <div class="card-content">
              <div class="number">{{accounts.filter(a => a.registered).length}}</div>
              <div class="text">个已注册</div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card class="stat-card">
            <template #header>
              <div class="card-header">
                <span>未注册账号</span>
                <el-tag type="warning">未激活</el-tag>
              </div>
            </template>
            <div class="card-content">
              <div class="number">{{accounts.filter(a => !a.registered).length}}</div>
              <div class="text">个未注册</div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <!-- 操作栏 -->
    <div class="action-bar">
      <div class="action-bar-content">
        <div class="action-bar-title">账号列表</div>
        <el-button type="primary" size="default" @click="openAddDialog">
          <el-icon>
            <Plus />
          </el-icon>添加账号
        </el-button>
      </div>
    </div>

    <!-- 表格 -->
    <el-card class="table-card">
      <el-table :data="accounts" style="width: 100%" border stripe highlight-current-row>
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="名称" min-width="120" />
        <el-table-column prop="host" label="主机" min-width="120" />
        <el-table-column prop="registered" label="注册状态" width="120">
          <template #default="scope">
            <el-tag :type="scope.row.registered ? 'success' : 'warning'" size="small">
              {{ scope.row.registered ? '已注册' : '未注册' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="180" fixed="right">
          <template #default="scope">
            <el-button-group>
              <el-button type="primary" size="small" @click="editAccount(scope.row)">
                <el-icon>
                  <Edit />
                </el-icon>
              </el-button>
              <el-button type="danger" size="small" @click="deleteAccount(scope.row.id)">
                <el-icon>
                  <Delete />
                </el-icon>
              </el-button>
            </el-button-group>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 添加/编辑对话框 -->
    <el-dialog v-model="dialogVisible" :title="editingAccount ? '编辑账号' : '添加账号'" width="500px" destroy-on-close>
      <el-form :model="newAccount" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="newAccount.name" placeholder="请输入账号名称" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="newAccount.pwd" placeholder="请输入密码" type="password" />
        </el-form-item>
        <el-form-item label="主机">
          <el-input v-model="newAccount.host" placeholder="请输入主机地址" />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="addAccount">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>
