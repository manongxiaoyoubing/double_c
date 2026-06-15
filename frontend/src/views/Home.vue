<template>
  <div class="home-container">
    <!-- Header 导航栏 -->
    <header class="header">
      <div class="header-content">
        <!-- 左侧 Logo 和系统名称 -->
        <div class="logo-section">
          <router-link to="/">
            <img 
              src="/img/logo.jpg" 
              alt="双碳合规审查系统" 
              class="logo-img"
              @error="handleImageError($event)"
            />
          </router-link>
          <span class="system-name">双碳合规审查系统</span>
        </div>
        
        <!-- 右侧导航菜单 -->
        <nav class="nav-menu">
          <router-link 
            v-for="item in navItems" 
            :key="item.path"
            :to="item.path"
            :class="['nav-item', { active: currentPath === item.path }]"
          >
            {{ item.name }}
          </router-link>
        </nav>
      </div>
    </header>

    <!-- Hero 主视觉区域 -->
    <section class="hero-section">
      <div class="hero-content">
        <!-- 左侧文字区域 -->
        <div class="hero-text">
          <h1 class="hero-title">双碳合规审查系统</h1>
          <p class="hero-description">
            基于 AI 的智能合规审查平台，助力企业双碳目标达成
          </p>
          <div class="cta-buttons">
            <router-link to="/login" class="btn btn-primary">
              立即体验
            </router-link>
            <router-link to="/login" class="btn btn-secondary">
              了解更多
            </router-link>
          </div>
        </div>
        
        <!-- 右侧 IP 形象区域 -->
        <div class="hero-character">
          <div class="character-wrapper">
            <img 
              src="/img/ip_character.png" 
              alt="碳小碳" 
              class="character-img"
              @error="handleImageError($event)"
            />
            <div class="glow-effect"></div>
          </div>
        </div>
      </div>
      
      <!-- 底部装饰条 -->
      <div class="hero-footer">
        <svg class="wave-svg" viewBox="0 0 1440 80" preserveAspectRatio="none">
          <path 
            fill="#f0f9ff" 
            d="M0,32L48,37.3C96,43,192,53,288,48C384,43,480,21,576,21.3C672,21,768,43,864,48C960,53,1056,43,1152,42.7C1248,43,1344,53,1392,58.7L1440,64L1440,80L1392,80C1344,80,1248,80,1152,80C1056,80,960,80,864,80C768,80,672,80,576,80C480,80,384,80,288,80C192,80,96,80,48,80L0,80Z"
          />
        </svg>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

// 导航菜单项
const navItems = [
  { name: '首页', path: '/' },
  { name: '合规审查', path: '/user/project-review' },
  { name: '数据填报', path: '/user/home' },
  { name: '碳核算', path: '/user/home' },
  { name: '系统管理', path: '/admin/dashboard' }
]

// 当前路径
const currentPath = ref(window.location.pathname)

// 监听路由变化
const handleRouteChange = () => {
  currentPath.value = window.location.pathname
}

// 图片加载失败处理
const handleImageError = (event: Event) => {
  const target = event.target as HTMLImageElement
  target.style.display = 'none'
}

onMounted(() => {
  window.addEventListener('popstate', handleRouteChange)
})

onUnmounted(() => {
  window.removeEventListener('popstate', handleRouteChange)
})
</script>

<style scoped>
/* 全局样式重置 */
.home-container {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  margin: 0;
  padding: 0;
  min-height: 100vh;
}

/* Header 导航栏 */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background: #ffffff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  z-index: 100;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-img {
  height: 40px;
  width: auto;
  border-radius: 4px;
}

.system-name {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
}

.nav-menu {
  display: flex;
  gap: 32px;
}

.nav-item {
  font-size: 14px;
  color: #606266;
  text-decoration: none;
  transition: color 0.3s ease;
  padding: 8px 0;
  position: relative;
}

.nav-item:hover {
  color: #409EFF;
}

.nav-item.active {
  color: #409EFF;
}

.nav-item.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: #409EFF;
  border-radius: 1px;
}

/* Hero 主视觉区域 */
.hero-section {
  padding-top: 64px;
  min-height: calc(100vh - 64px);
  background: linear-gradient(135deg, #0a1628 0%, #1a3a5c 50%, #0d2137 100%);
  position: relative;
  overflow: hidden;
}

.hero-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
  min-height: calc(100vh - 144px);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

/* 左侧文字区域 */
.hero-text {
  flex: 0 0 50%;
  max-width: 50%;
}

.hero-title {
  font-size: 48px;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.2;
  margin: 0 0 24px 0;
}

.hero-description {
  font-size: 18px;
  color: rgba(255, 255, 255, 0.85);
  line-height: 1.6;
  margin: 0 0 40px 0;
  max-width: 500px;
}

.cta-buttons {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 32px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.3s ease;
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: #409EFF;
  color: #ffffff;
}

.btn-primary:hover {
  background: #66b1ff;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(64, 158, 255, 0.4);
}

.btn-secondary {
  background: transparent;
  color: #ffffff;
  border: 2px solid #ffffff;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.8);
}

/* 右侧 IP 形象区域 */
.hero-character {
  flex: 0 0 50%;
  max-width: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.character-wrapper {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.character-img {
  max-width: 400px;
  width: 100%;
  height: auto;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

.glow-effect {
  position: absolute;
  bottom: -20px;
  width: 300px;
  height: 80px;
  background: radial-gradient(ellipse at center, rgba(64, 158, 255, 0.3) 0%, transparent 70%);
  border-radius: 50%;
}

/* 底部装饰条 */
.hero-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 80px;
}

.wave-svg {
  width: 100%;
  height: 100%;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .header-content {
    padding: 0 16px;
  }
  
  .system-name {
    display: none;
  }
  
  .nav-menu {
    gap: 16px;
  }
  
  .nav-item {
    font-size: 13px;
  }
  
  .hero-content {
    flex-direction: column;
    text-align: center;
    padding: 40px 16px;
    min-height: auto;
  }
  
  .hero-text {
    flex: 1;
    max-width: 100%;
    margin-bottom: 40px;
  }
  
  .hero-title {
    font-size: 32px;
  }
  
  .hero-description {
    font-size: 16px;
    max-width: 100%;
    margin: 0 0 32px 0;
  }
  
  .hero-character {
    flex: 1;
    max-width: 100%;
  }
  
  .character-img {
    max-width: 300px;
  }
  
  .cta-buttons {
    justify-content: center;
  }
  
  .glow-effect {
    width: 200px;
    height: 60px;
  }
}

@media (max-width: 480px) {
  .nav-menu {
    gap: 12px;
  }
  
  .nav-item {
    font-size: 12px;
  }
  
  .hero-title {
    font-size: 28px;
  }
  
  .hero-description {
    font-size: 14px;
  }
  
  .btn {
    padding: 10px 24px;
    font-size: 13px;
  }
  
  .character-img {
    max-width: 250px;
  }
}
</style>