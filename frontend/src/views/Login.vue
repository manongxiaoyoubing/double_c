<template>
  <div class="login-container">
    <!-- 顶部导航栏 -->
    <header class="nav-header">
      <div class="nav-inner">
        <!-- 左侧 Logo + 系统名称 -->
        <div class="nav-brand">
          <img src="/img/logo.jpg" alt="双碳合规审查系统" class="nav-logo" />
        </div>
        <!-- 中间导航菜单 -->
        <nav class="nav-menu">
          <a href="#" class="nav-item active">首页</a>
          <a href="#" class="nav-item">政策问答</a>
          <a href="#" class="nav-item">项目审查</a>
          <a href="#" class="nav-item">个人中心</a>
        </nav>
        <!-- 右侧用户头像占位 -->
        <div class="nav-avatar">
          <img v-if="false" src="" alt="" />
        </div>
      </div>
    </header>

    <!-- 主内容区域 -->
    <main class="main-content">
      <!-- 左侧文字区 -->
      <div class="left-section">
        <h1 class="greeting-title">Hi~ 我是碳小碳</h1>
        <h2 class="greeting-subtitle">您的双碳合规审查小助手</h2>

        <!-- 登录表单卡片 -->
        <div class="login-card">
          <el-form :model="loginForm" :rules="rules" ref="formRef" class="login-form" size="large">
            <el-form-item prop="username">
              <el-input
                v-model="loginForm.username"
                placeholder="请输入用户名"
                :prefix-icon="User"
                clearable
              />
            </el-form-item>
            <el-form-item prop="password">
              <el-input
                v-model="loginForm.password"
                type="password"
                placeholder="请输入密码"
                :prefix-icon="Lock"
                show-password
                @keyup.enter="handleLogin"
              />
            </el-form-item>
            <el-form-item>
              <el-button
                type="primary"
                @click="handleLogin"
                :loading="loading"
                class="login-btn"
              >
                {{ loading ? '登录中...' : '登 录' }}
              </el-button>
            </el-form-item>
          </el-form>

          <div class="test-accounts">
            <p class="accounts-title">测试账号：</p>
            <p class="account-row"><span class="label">管理员：</span><span>admin / admin123</span></p>
            <p class="account-row"><span class="label">普通用户：</span><span>user / user123</span></p>
          </div>
        </div>

        <!-- 底部描述文字 -->
        <p class="desc-text">精准匹配国家"1+N"双碳政策体系</p>
        <p class="desc-text desc-text-sm">政策问答 · 项目审查 · 合规报告一键生成</p>
      </div>

    <!-- 右侧 IP 形象区 -->
    <div class="right-section">
      <div class="ip-wrapper">
        <img src="/img/ip_character.png" alt="碳小碳" class="ip-character" />
      </div>
      <!-- IP 周围的环境光斑装饰 -->
      <div class="ip-ambient-glow"></div>
      <span class="ip-light-spot spot-1"></span>
      <span class="ip-light-spot spot-2"></span>
      <span class="ip-light-spot spot-3"></span>
    </div>
    </main>

    <!-- 底部装饰条（弧形叶子装饰） -->
    <footer class="bottom-decoration">
      <svg viewBox="0 0 1440 160" preserveAspectRatio="none" class="decoration-svg">
        <!-- 弧形背景 -->
        <path d="M0,80 Q360,10 720,60 T1440,80 L1440,160 L0,160 Z" fill="#e8f5e9" opacity="0.6"/>
        <path d="M0,100 Q360,40 720,80 T1440,100 L1440,160 L0,160 Z" fill="#d4edda" opacity="0.5"/>
        <!-- 叶子 - 黄色 -->
        <ellipse cx="280" cy="110" rx="55" ry="28" fill="#e6ee58" transform="rotate(-25 280 110)" opacity="0.8"/>
        <ellipse cx="280" cy="110" rx="30" ry="14" fill="#cddc39" transform="rotate(-25 280 110)" opacity="0.3"/>
        <!-- 叶子 - 浅蓝 -->
        <ellipse cx="520" cy="120" rx="50" ry="24" fill="#b3e5fc" transform="rotate(10 520 120)" opacity="0.75"/>
        <ellipse cx="520" cy="120" rx="26" ry="12" fill="#81d4fa" transform="rotate(10 520 120)" opacity="0.3"/>
        <!-- 回收标志 -->
        <g transform="translate(720, 85)">
          <circle cx="0" cy="15" r="22" fill="none" stroke="#a5d6a7" stroke-width="4" opacity="0.6"/>
          <path d="M-12,5 L-18,20 L-6,20 M-10,10 L-16,10 M6,5 L12,20 L0,20 M8,10 L2,10" stroke="#a5d6a7" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.6"/>
          <path d="M-3,27 A8,8 0 1,1 5,23" stroke="#a5d6a7" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.6"/>
          <polyline points="3,29 6,26 8,29" stroke="#a5d6a7" stroke-width="2" fill="none" opacity="0.6"/>
        </g>
        <!-- 小圆点装饰 -->
        <circle cx="200" cy="130" r="5" fill="#c5e1a5" opacity="0.6"/>
        <circle cx="400" cy="140" r="4" fill="#fff59d" opacity="0.5"/>
        <circle cx="600" cy="135" r="6" fill="#b3e5fc" opacity="0.45"/>
        <circle cx="900" cy="138" r="4" fill="#a5d6a7" opacity="0.5"/>
        <circle cx="1120" cy="132" r="5" fill="#fff59d" opacity="0.45"/>
        <circle cx="1280" cy="142" r="4" fill="#b3e5fc" opacity="0.5"/>
      </svg>
    </footer>

    <!-- 浮动叶子装饰 -->
    <div class="floating-decor leaf-left">
      <svg width="70" height="95" viewBox="0 0 70 95">
        <defs>
          <linearGradient id="leafGradL" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#c8e6c9;stop-opacity:0.9" />
            <stop offset="100%" style="stop-color:#81c784;stop-opacity:0.7" />
          </linearGradient>
        </defs>
        <path d="M35,5 Q65,30 55,65 Q35,90 15,65 Q5,30 35,5Z" fill="url(#leafGradL)"/>
        <path d="M35,15 Q35,55 35,80" stroke="#a5d6a7" stroke-width="1.5" fill="none" opacity="0.5"/>
        <path d="M35,35 Q48,32 52,38" stroke="#a5d6a7" stroke-width="1.2" fill="none" opacity="0.4"/>
        <path d="M35,50 Q22,47 18,53" stroke="#a5d6a7" stroke-width="1.2" fill="none" opacity="0.4"/>
      </svg>
    </div>
    <div class="floating-decor leaf-right">
      <svg width="50" height="68" viewBox="0 0 50 68">
        <defs>
          <linearGradient id="leafGradR" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#b2dfdb;stop-opacity:0.8" />
            <stop offset="100%" style="stop-color:#4db6ac;stop-opacity:0.6" />
          </linearGradient>
        </defs>
        <path d="M25,3 Q46,22 39,48 Q25,66 11,48 Q4,22 25,3Z" fill="url(#leafGradR)"/>
        <path d="M25,10 Q25,40 25,58" stroke="#80cbc4" stroke-width="1.2" fill="none" opacity="0.5"/>
      </svg>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { User, Lock } from '@element-plus/icons-vue'
import { authApi } from '../api/index'

const router = useRouter()
const formRef = ref()
const loading = ref(false)

const loginForm = reactive({
  username: '',
  password: ''
})

const rules = {
  username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
}

const handleLogin = async () => {
  const valid = await formRef.value?.validate().catch(() => false)
  if (!valid) return

  loading.value = true

  try {
    const res = await authApi.login(loginForm.username, loginForm.password)
    if (res.code === 200) {
      localStorage.setItem('username', res.data.username)
      localStorage.setItem('role', res.data.role)
      ElMessage.success('登录成功')
      setTimeout(() => {
        if (res.data.role === 'admin') {
          router.push('/admin/dashboard')
        } else {
          router.push('/user/home')
        }
      }, 300)
    } else {
      ElMessage.error(res.message || '登录失败')
    }
  } catch (err: any) {
    const msg = err.response?.data?.message || '网络错误，请稍后重试'
    ElMessage.error(msg)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* ========== 容器 & 背景 ========== */
.login-container {
  min-height: 100vh;
  width: 100%;
  background: linear-gradient(135deg, #f7fae6 0%, #ecf8ed 25%, #dff6f3 55%, #d4eff8 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  font-family: 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif;
}

/* ========== 导航栏 ========== */
.nav-header {
  height: 64px;
  display: flex;
  align-items: center;
  background: transparent;
  border-bottom: none;
  position: relative;
  z-index: 100;
}

.nav-inner {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-brand {
  display: flex;
  align-items: center;
}

.nav-logo {
  height: 38px;
  width: auto;
  object-fit: contain;
  border-radius: 50%;
}

.nav-menu {
  display: flex;
  gap: 36px;
}

.nav-item {
  font-size: 15px;
  color: #546e7a;
  text-decoration: none;
  position: relative;
  padding: 4px 0;
  transition: color 0.25s ease;
  font-weight: 500;
}

.nav-item:hover,
.nav-item.active {
  color: #43a047;
}

.nav-item.active::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  width: 20px;
  height: 3px;
  background: #43a047;
  border-radius: 2px;
}

.nav-avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: linear-gradient(135deg, #fce4ec, #f8bbd9);
  cursor: pointer;
  transition: transform 0.2s ease;
}

.nav-avatar:hover {
  transform: scale(1.08);
}

/* ========== 主内容区 ========== */
.main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 1140px;
  margin: 0 auto;
  padding: 40px;
  gap: 60px;
  position: relative;
  z-index: 10;
}

/* ----- 左侧 ----- */
.left-section {
  flex: 1;
  max-width: 540px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.greeting-title {
  font-size: 42px;
  font-weight: 700;
  background: linear-gradient(135deg, #26a69a, #00acc1);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0 0 10px 0;
  line-height: 1.25;
  letter-spacing: 1px;
}

.greeting-subtitle {
  font-size: 26px;
  font-weight: 600;
  background: linear-gradient(135deg, #42b883, #26a69a);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0 0 32px 0;
  line-height: 1.3;
  letter-spacing: 1px;
}

/* 登录卡片 */
.login-card {
  background: rgba(255, 255, 255, 0.82);
  backdrop-filter: blur(16px);
  border-radius: 20px;
  padding: 32px 36px;
  box-shadow:
    0 8px 32px rgba(76, 175, 80, 0.1),
    0 2px 8px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.85);
  margin-bottom: 28px;
}

/* 覆盖 Element Plus 默认样式 */
.login-card :deep(.el-input__wrapper) {
  border-radius: 10px;
  padding: 4px 12px;
  box-shadow: 0 0 0 1px #e0e0e0 inset;
  background: #fafafa;
  transition: all 0.25s ease;
}

.login-card :deep(.el-input__wrapper:hover) {
  box-shadow: 0 0 0 1px #81c784 inset;
}

.login-card :deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 1px #66bb6a inset, 0 0 0 3px rgba(102, 187, 106, 0.12);
  background: #fff;
}

.login-card :deep(.el-form-item) {
  margin-bottom: 20px;
}

.login-card :deep(.el-form-item:last-child) {
  margin-bottom: 0;
}

.login-btn {
  width: 100%;
  height: 46px;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  background: linear-gradient(135deg, #66bb6a, #43a047);
  border: none;
  letter-spacing: 4px;
  transition: all 0.3s ease;
}

.login-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(67, 160, 71, 0.35);
}

.login-btn:active:not(:disabled) {
  transform: translateY(0);
}

.test-accounts {
  background: linear-gradient(135deg, #f1f8e9, #e8f5e9);
  border-radius: 10px;
  padding: 14px 16px;
  margin-top: 18px;
}

.accounts-title {
  font-size: 13px;
  color: #558b2f;
  font-weight: 500;
  margin: 0 0 8px 0;
}

.account-row {
  font-size: 12px;
  color: #666;
  margin: 4px 0;
}

.account-row .label {
  color: #999;
}

.desc-text {
  font-size: 14px;
  color: #607d8b;
  margin: 0 0 4px 0;
  letter-spacing: 0.5px;
}

.desc-text-sm {
  font-size: 13px;
  color: #78909c;
}

/* ----- 右侧 IP 形象 ----- */
.right-section {
  flex: 1;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  max-width: 480px;
  padding-bottom: 10px;
  position: relative;
}

.ip-wrapper {
  position: relative;
  animation: floatIP 3s ease-in-out infinite;
}

/* IP 形象底部的地面阴影 —— 椭圆形真实投影 */
.ip-wrapper::before {
  content: '';
  position: absolute;
  bottom: -18px;
  left: 50%;
  transform: translateX(-50%);
  width: 70%;
  height: 28px;
  background: radial-gradient(ellipse at 50% 55%, rgba(38, 166, 154, 0.35) 0%, rgba(38, 166, 154, 0.15) 40%, transparent 70%);
  border-radius: 50%;
  filter: blur(8px);
  animation: shadowFloat 3s ease-in-out infinite;
}

/* 底部环境光晕 —— 让图片底部柔和融入背景 */
.ip-wrapper::after {
  content: '';
  position: absolute;
  bottom: -30px;
  left: 50%;
  transform: translateX(-50%);
  width: 90%;
  height: 60px;
  background: radial-gradient(ellipse at 50% 60%, rgba(200, 240, 220, 0.45) 0%, rgba(180, 230, 210, 0.2) 35%, transparent 65%);
  border-radius: 50%;
  filter: blur(14px);
  pointer-events: none;
}

.ip-character {
  display: block;
  max-width: 380px;
  width: 100%;
  height: auto;
  object-fit: contain;
  /* 多层柔和投影 + 环境光 */
  filter:
    drop-shadow(0 16px 36px rgba(38, 166, 154, 0.20))
    drop-shadow(0 6px 16px rgba(77, 182, 172, 0.15))
    drop-shadow(0 2px 4px rgba(0, 0, 0, 0.06));
}

@keyframes floatIP {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-16px); }
}

/* 阴影跟随浮动动画同步缩放 */
@keyframes shadowFloat {
  0%, 100% { transform: translateX(-50%) scale(1); opacity: 0.7; }
  50% { transform: translateX(-50%) scale(0.78); opacity: 0.35; }
}

/* IP 周围的环境光晕 —— 大面积柔光 */
.ip-ambient-glow {
  position: absolute;
  bottom: 10%;
  left: 50%;
  transform: translateX(-50%);
  width: 320px;
  height: 280px;
  background: radial-gradient(ellipse at 50% 65%, rgba(178, 223, 219, 0.35) 0%, rgba(200, 240, 230, 0.18) 40%, transparent 70%);
  border-radius: 50%;
  filter: blur(30px);
  pointer-events: none;
  z-index: -1;
}

/* IP 附近的光斑粒子 */
.ip-light-spot {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  z-index: -1;
}

.spot-1 {
  width: 14px;
  height: 14px;
  top: 20%;
  left: 12%;
  background: radial-gradient(circle, rgba(165, 214, 167, 0.55) 0%, transparent 70%);
  animation: spotFloat 5s ease-in-out infinite;
}

.spot-2 {
  width: 10px;
  height: 10px;
  top: 35%;
  right: 15%;
  background: radial-gradient(circle, rgba(129, 212, 250, 0.45) 0%, transparent 70%);
  animation: spotFloat 6s ease-in-out infinite 1.5s;
}

.spot-3 {
  width: 8px;
  height: 8px;
  bottom: 25%;
  left: 20%;
  background: radial-gradient(circle, rgba(200, 230, 201, 0.4) 0%, transparent 70%);
  animation: spotFloat 4.5s ease-in-out infinite 0.8s;
}

@keyframes spotFloat {
  0%, 100% { opacity: 0.6; transform: translateY(0) scale(1); }
  50% { opacity: 0.3; transform: translateY(-10px) scale(0.85); }
}

/* ========== 底部装饰条 ========== */
.bottom-decoration {
  position: relative;
  width: 100%;
  height: 150px;
  overflow: hidden;
  pointer-events: none;
  z-index: 1;
}

.decoration-svg {
  width: 100%;
  height: 100%;
  display: block;
}

/* ========== 浮动叶子装饰 ========== */
.floating-decor {
  position: absolute;
  z-index: 2;
  pointer-events: none;
  opacity: 0.55;
}

.leaf-left {
  bottom: 180px;
  left: 5%;
  animation: leafFloat 6s ease-in-out infinite;
}

.leaf-right {
  top: 25%;
  right: 6%;
  animation: leafFloat 7s ease-in-out infinite reverse;
}

@keyframes leafFloat {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(6deg); }
}

/* ========== 响应式适配 ========== */
@media (max-width: 960px) {
  .main-content {
    flex-direction: column;
    gap: 30px;
    padding: 24px 20px;
  }

  .left-section {
    max-width: 480px;
    align-items: center;
    text-align: center;
  }

  .greeting-title {
    font-size: 32px;
  }

  .greeting-subtitle {
    font-size: 20px;
  }

  .right-section {
    max-width: 300px;
  }

  .ip-character {
    max-width: 260px;
  }

  .nav-menu {
    gap: 20px;
  }

  .nav-item {
    font-size: 14px;
  }

  .nav-inner {
    padding: 0 20px;
  }
}

@media (max-width: 600px) {
  .nav-header {
    height: 56px;
  }

  .nav-menu {
    display: none;
  }

  .greeting-title {
    font-size: 26px;
  }

  .greeting-subtitle {
    font-size: 17px;
  }

  .login-card {
    padding: 24px 20px;
    width: 100%;
    max-width: 340px;
  }

  .bottom-decoration {
    height: 100px;
  }

  .floating-decor {
    display: none;
  }
}
</style>
