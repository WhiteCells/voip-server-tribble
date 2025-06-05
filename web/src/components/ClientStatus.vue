<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { clientApi, accountApi } from '../api'
import { ElMessage } from 'element-plus'
import '@/assets/style.css'
import type { Client } from '@/types/Client'

interface Client {
  id: number
  name: string
  status: '在线' | '离线'
  accounts: Account[]
}

const clients = ref<Client[]>([])
const accounts = ref<Account[]>([])
const newClient = ref({ name: '', accounts: [] as number[] })
const dialogVisible = ref(false)
const editingClient = ref<Client | null>(null)

// 计算属性：获取未注册的账号列表
const unregisteredAccounts = computed(() => {
  return accounts.value.filter(account => account.status === '未注册')
})

// 获取客户端列表
const fetchClients = async () => {
  try {
    const response = await clientApi.getClients()
    clients.value = response.data
  } catch (error: any) {
    ElMessage.error(error.message || '获取客户端列表失败')
  }
}

// 获取账号列表
const fetchAccounts = async () => {
  try {
    const response = await accountApi.getAccounts()
    accounts.value = response.data
  } catch (error: any) {
    ElMessage.error(error.message || '获取账号列表失败')
  }
}

// 添加或更新客户端
const addClient = async () => {
  try {
    const selectedAccounts = accounts.value.filter(acc => newClient.value.accounts.includes(acc.id))
    const clientData = {
      name: newClient.value.name,
      accounts: selectedAccounts
    }

    if (editingClient.value) {
      // 更新现有客户端
      await clientApi.updateClient(editingClient.value.id, clientData)
      ElMessage.success('更新客户端成功')
    } else {
      // 添加新客户端
      await clientApi.addClient(clientData)
      ElMessage.success('添加客户端成功')
    }
    dialogVisible.value = false
    newClient.value = { name: '', accounts: [] }
    editingClient.value = null
    fetchClients() // 刷新列表
  } catch (error: any) {
    ElMessage.error(error.message || (editingClient.value ? '更新客户端失败' : '添加客户端失败'))
  }
}

// 编辑客户端
const editClient = (client: Client) => {
  editingClient.value = client
  newClient.value = {
    name: client.name,
    accounts: client.accounts.map(acc => acc.id)
  }
  dialogVisible.value = true
}

// 删除客户端
const deleteClient = async (id: number) => {
  try {
    await clientApi.deleteClient(id)
    ElMessage.success('删除客户端成功')
    fetchClients() // 刷新列表
  } catch (error: any) {
    ElMessage.error(error.message || '删除客户端失败')
  }
}

// 打开添加对话框
const openAddDialog = () => {
  editingClient.value = null
  newClient.value = { name: '', accounts: [] }
  dialogVisible.value = true
}

// 组件挂载时获取数据
onMounted(() => {
  fetchClients()
  fetchAccounts()
})
</script>

<template>
  <div class="client-status">
    <!-- 统计卡片 -->
    <div class="stat-cards">
      <el-row :gutter="20">
        <el-col :span="8">
          <el-card class="stat-card">
            <template #header>
              <div class="card-header">
                <span>总客户端数</span>
                <el-tag type="info">总数</el-tag>
              </div>
            </template>
            <div class="card-content">
              <div class="number">{{ clients.length }}</div>
              <div class="text">个客户端</div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card class="stat-card">
            <template #header>
              <div class="card-header">
                <span>在线客户端</span>
                <el-tag type="success">在线</el-tag>
              </div>
            </template>
            <div class="card-content">
              <div class="number">{{clients.filter(c => c.status === '在线').length}}</div>
              <div class="text">个在线</div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card class="stat-card">
            <template #header>
              <div class="card-header">
                <span>离线客户端</span>
                <el-tag type="info">离线</el-tag>
              </div>
            </template>
            <div class="card-content">
              <div class="number">{{clients.filter(c => c.status === '离线').length}}</div>
              <div class="text">个离线</div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <!-- 操作栏 -->
    <div class="action-bar">
      <div class="action-bar-content">
        <div class="action-bar-title">客户端列表</div>
        <el-button type="primary" @click="openAddDialog" size="default">
          <el-icon>
            <Plus />
          </el-icon>添加客户端
        </el-button>
      </div>
    </div>

    <!-- 数据表格 -->
    <el-card class="table-card">
      <el-table :data="clients" style="width: 100%" border stripe highlight-current-row>
        <el-table-column prop="id" label="ID" width="100" />
        <el-table-column prop="uuid" label="UUID" width="200" />
        <el-table-column prop="name" label="名称" width="180" />
        <el-table-column prop="status" label="状态" width="100">
          <template #default="{ row }">
            <el-tag :type="row.status === '在线' ? 'success' : 'info'">
              {{ row.status }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="{ row }">
            <el-button-group>
              <el-button type="primary" @click="editClient(row)" size="small">
                <el-icon>
                  <Edit />
                </el-icon>
              </el-button>
              <el-button type="danger" @click="deleteClient(row.id)" size="small">
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
    <el-dialog v-model="dialogVisible" :title="添加客户端" width="500px" destroy-on-close>
      <el-form :model="newClient" label-width="80px">
        <el-form-item label="名称" required>
          <el-input v-model="newClient.name" placeholder="请输入客户端名称" />
        </el-form-item>
        <!-- <el-form-item label="账号" required>
          <el-select v-model="newClient.accounts" multiple filterable placeholder="请选择未注册账号" style="width: 100%">
            <el-option v-for="account in unregisteredAccounts" :key="account.id" :label="account.name"
              :value="account.id">
              <div style="display: flex; align-items: center; justify-content: space-between">
                <span>{{ account.name }}</span>
                <el-tag size="small" type="warning">
                  未注册
                </el-tag>
              </div>
            </el-option>
          </el-select>
          <div class="form-tip" v-if="unregisteredAccounts.length === 0">
            当前没有可用的未注册账号
          </div>
        </el-form-item> -->
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="addClient">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>
