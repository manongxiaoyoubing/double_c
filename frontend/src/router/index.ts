import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/user/home',
      name: 'UserHome',
      component: () => import('../views/user/Home.vue'),
      meta: { requiresAuth: true, role: 'user' }
    },
    {
      path: '/user/policy-qa',
      name: 'PolicyQA',
      component: () => import('../views/user/PolicyQA.vue'),
      meta: { requiresAuth: true, role: 'user' }
    },
    {
      path: '/user/project-review',
      name: 'ProjectReview',
      component: () => import('../views/user/ProjectReview.vue'),
      meta: { requiresAuth: true, role: 'user' }
    },
    {
      path: '/user/report-download',
      name: 'ReportDownload',
      component: () => import('../views/user/ReportDownload.vue'),
      meta: { requiresAuth: true, role: 'user' }
    },
    {
      path: '/admin/dashboard',
      name: 'AdminDashboard',
      component: () => import('../views/admin/Dashboard.vue'),
      meta: { requiresAuth: true, role: 'admin' }
    },
    {
      path: '/admin/policy-manage',
      name: 'PolicyManage',
      component: () => import('../views/admin/PolicyManage.vue'),
      meta: { requiresAuth: true, role: 'admin' }
    }
  ]
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const role = localStorage.getItem('role')
  
  if (to.meta.requiresAuth && !role) {
    next('/login')
  } else if (to.meta.role && to.meta.role !== role) {
    next('/login')
  } else {
    next()
  }
})

export default router
