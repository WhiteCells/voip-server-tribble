<script setup lang="ts">
import { ref } from 'vue'
import '../assets/style.css'

interface Call {
  id: number
  phoneNumber: string
  status: '空闲' | '拨打中' | '已完成'
}

const calls = ref<Call[]>([
  { id: 1, phoneNumber: '13800138000', status: '空闲' },
  { id: 2, phoneNumber: '13900139000', status: '拨打中' }
])

const newCall = ref({ phoneNumber: '' })
const dialogVisible = ref(false)
const editingCall = ref<Call | null>(null)

const addCall = () => {
  if (editingCall.value) {
    // 编辑现有通话
    const index = calls.value.findIndex(c => c.id === editingCall.value?.id)
    if (index !== -1) {
      calls.value[index] = { ...editingCall.value, ...newCall.value }
    }
  } else {
    // 添加新通话
    const id = calls.value.length + 1
    calls.value.push({ ...newCall.value, id, status: '空闲' })
  }
  dialogVisible.value = false
  newCall.value = { phoneNumber: '' }
  editingCall.value = null
}

const editCall = (call: Call) => {
  editingCall.value = call
  newCall.value = { phoneNumber: call.phoneNumber }
  dialogVisible.value = true
}

const deleteCall = (id: number) => {
  calls.value = calls.value.filter(call => call.id !== id)
}
</script>

<template>
  <div class="call-status">
    <!-- 统计卡片 -->
    <div class="stat-cards">
      <el-row :gutter="20">
        <el-col :span="8">
          <el-card class="stat-card">
            <template #header>
              <div class="card-header">
                <span>总通话数</span>
                <el-tag type="info">总数</el-tag>
              </div>
            </template>
            <div class="card-content">
              <div class="number">{{ calls.length }}</div>
              <div class="text">个通话</div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card class="stat-card">
            <template #header>
              <div class="card-header">
                <span>拨打中</span>
                <el-tag type="warning">进行中</el-tag>
              </div>
            </template>
            <div class="card-content">
              <div class="number">{{calls.filter(c => c.status === '拨打中').length}}</div>
              <div class="text">个进行中</div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card class="stat-card">
            <template #header>
              <div class="card-header">
                <span>已完成</span>
                <el-tag type="success">已完成</el-tag>
              </div>
            </template>
            <div class="card-content">
              <div class="number">{{calls.filter(c => c.status === '已完成').length}}</div>
              <div class="text">个已完成</div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <!-- 操作栏 -->
    <div class="action-bar">
      <div class="action-bar-content">
        <div class="action-bar-title">手机号列表</div>
        <el-button type="primary" size="default" @click="dialogVisible = true">
          <el-icon>
            <Plus />
          </el-icon>添加手机号
        </el-button>
      </div>
    </div>

    <!-- 表格 -->
    <el-card class="table-card">
      <el-table :data="calls" style="width: 100%" border stripe highlight-current-row>
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="phoneNumber" label="手机号" min-width="120" />
        <el-table-column prop="status" label="拨打状态" width="120">
          <template #default="scope">
            <el-tag :type="scope.row.status === '空闲' ? 'info' : scope.row.status === '拨打中' ? 'warning' : 'success'"
              size="small">
              {{ scope.row.status }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="scope">
            <el-button-group>
              <el-button type="primary" size="small" @click="editCall(scope.row)">
                <el-icon>
                  <Edit />
                </el-icon>
              </el-button>
              <el-button type="danger" size="small" @click="deleteCall(scope.row.id)">
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
    <el-dialog v-model="dialogVisible" :title="添加手机号" width="500px" destroy-on-close>
      <el-form :model="newCall" label-width="80px">
        <el-form-item label="手机号" required>
          <el-input v-model="newCall.phoneNumber" placeholder="请输入手机号" />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="addCall">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>