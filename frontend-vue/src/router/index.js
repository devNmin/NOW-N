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
    // 아이디 찾기
    path: '/findId',
    name: 'findId',
    component: () => import('@/components/user/FindId.vue')
  },
  {
    // 회원가입
    path: '/signUp',
    name: 'signUp',
    component: () => import('@/components/user/RegistForm.vue')
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
  },
  {
    // 트레이너
    path: '/trainer',
    name: 'trainer',
    component: () => import('@/views/trainer/TrainerView.vue')

  },
  {
    // 트레이너 디테일
    path: '/trainer/detail',
    name: 'trainerDetail',
    component: () => import('@/views/trainer/TrainerDetailView.vue')
  },
  {
    // 트레이너 신청
    path: '/trainer/apply',
    name: 'trainerApply',
    component: () => import('@/views/trainer/TrainerApplyView.vue')
  },
  {
    // 트레이너 스케쥴
    path: '/trainer/schedule',
    name: 'trainerSchedule',
    component: () => import('@/views/trainer/TrainerScheduleView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
