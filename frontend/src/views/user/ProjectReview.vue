<template>
  <div>
    <h2>项目合规审查</h2>
    <el-form :model="form" label-width="120px">
      <el-form-item label="项目名称">
        <el-input v-model="form.project_name" />
      </el-form-item>
      <el-form-item label="所属行业">
        <el-input v-model="form.industry" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submit">提交审查</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { reviewApi } from '../../api/index'

const form = reactive({
  project_name: '',
  industry: ''
})

const submit = async () => {
  await reviewApi.submit(form)
  alert('审查已提交')
}
</script>

<style scoped>
</style>
