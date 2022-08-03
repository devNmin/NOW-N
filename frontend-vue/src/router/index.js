import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    // 홈 페이지
    path: '/',
    name: 'home',
    component: () => import('@/views/HomeView.vue')
  },
  {
    // 로그인
    path: '/login',
    name: 'login',
    component: () => import('@/views/user/LoginView.vue')
  },
  {
    // 회원가입
    path: '/users/regist',
    name: 'RegistView',
    component: () => import('@/views/user/RegistView.vue')
  },
  {
    // 아이디찾기
    path: '/users/findid',
    name: 'FindId',
    component: () => import('@/components/user/FindId.vue')
  },
  {
    // 비밀번호찾기
    path: '/users/findpw',
    name: 'FindPw',
    component: () => import('@/components/user/FindPw.vue')
  },
  {
    // 프로필
    path: '/profile/getprofile/',
    name: 'profile',
    component: () => import('@/components/user/UserProfile.vue')
  },
  {
    // Gx룸
    path: '/GX',
    name: 'gxroom',
    component: () => import('@/views/room/GxRoom.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
