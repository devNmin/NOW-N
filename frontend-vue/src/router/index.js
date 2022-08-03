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
    // 회원가입
    path: '/users/regist',
    name: 'RegistUser',
    component: () => import('@/components/user/RegistUser.vue')
  },
  {
    // 프로필
    path: '/profile/getprofile/',
    name: 'profile',
    component: () => import('@/components/user/UserProfile.vue')
  },
  {
    // G.X
    path: '/GX/getlist/',
    name: 'GX',
    component: () => import('@/views/gx/GroupXerciseView.vue')
  },
  {
    // G.X 메인페이지(G.X 페이지와 동일하다)
    path: '/GX/',
    name: 'GX-main',
    component: () => import('@/views/gx/GroupXerciseView.vue')
  },
  {
    // 방생성 모달 임시로 사용하는 주소
    path: '/GX/Room',
    name: 'makeroom',
    component: () => import('@/views/gx/GroupXerciseView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
