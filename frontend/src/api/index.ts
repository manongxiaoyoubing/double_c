import axios, { AxiosInstance } from 'axios'
import { ElMessage } from 'element-plus'

const api: AxiosInstance = axios.create({
  baseURL: '/api',
  timeout: 60000,
  withCredentials: true
})

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    const msg = error.response?.data?.message || '网络错误，请稍后重试'
    ElMessage.error(msg)
    return Promise.reject(error)
  }
)

// API 对象
export const authApi = {
  login: (username: string, password: string) =>
    api.post('/auth/login', { username, password }),
  logout: () => api.post('/auth/logout'),
  getMe: () => api.get('/auth/me')
}

export const policyApi = {
  list: () => api.get('/policy/list'),
  upload: (formData: FormData) => api.post('/policy/upload', formData),
  delete: (id: number) => api.delete(`/policy/${id}`)
}

export const qaApi = {
  ask: (question: string, policyId?: number) =>
    api.post('/qa/ask', { question, policy_id: policyId }),
  history: () => api.get('/qa/history')
}

export const reviewApi = {
  submit: (data: any) => api.post('/review/submit', data),
  getResult: (id: number) => api.get(`/review/${id}`),
  history: () => api.get('/review/history')
}

export default api
