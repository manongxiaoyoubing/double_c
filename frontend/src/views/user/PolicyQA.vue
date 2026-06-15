<template>
  <div>
    <h2>政策智能问答</h2>
    <el-input v-model="question" placeholder="请输入关于政策的问题" />
    <el-button @click="ask">提问</el-button>
    <div v-if="answer">{{ answer }}</div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { qaApi } from '../../api/index'

const question = ref('')
const answer = ref('')

const ask = async () => {
  const res = await qaApi.ask(question.value)
  answer.value = res.data.answer
}
</script>

<style scoped>
</style>
