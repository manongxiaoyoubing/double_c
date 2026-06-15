<template>
  <div>
    <h2>政策管理</h2>
    <el-button type="primary" @click="uploadDialogVisible = true">上传政策</el-button>
    <el-table :data="policies" style="margin-top: 20px">
      <el-table-column prop="title" label="政策标题" />
      <el-table-column prop="industry" label="所属行业" />
      <el-table-column prop="status" label="状态" />
      <el-table-column label="操作">
        <template #default="scope">
          <el-button size="small" @click="deletePolicy(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { policyApi } from '../../api/index'

const policies = ref([])
const uploadDialogVisible = ref(false)

const loadPolicies = async () => {
  const res = await policyApi.list()
  policies.value = res.data
}

const deletePolicy = async (id: number) => {
  await policyApi.delete(id)
  loadPolicies()
}

onMounted(() => {
  loadPolicies()
})
</script>

<style scoped>
</style>
