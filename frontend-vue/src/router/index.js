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
    component: () => import('@/views/gx/MakeRoomView.vue')
  },
  {
    // P.X 식단 다이어리
    path: '/PT/diet/getcalorie',
    name: 'diet-diary',
    component: () => import('@/components/px/DietDiary.vue')
  },
  {
    // P.X 코칭룸
    path: '/PT/onetoone/enterroom/',
    name: 'coachingroom',
    component: () => import('@/components/px/CoachingRoom.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
