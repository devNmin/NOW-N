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
    path: '/profiles',
    name: 'profile',
    component: () => import('@/views/user/UserProfileView.vue')
  },
  {
    // G.X 메인페이지
    path: '/GX/',
    name: 'GX-main',
    component: () => import('@/views/gx/GroupXerciseView.vue')
  },
  {
    // gx 방 생성모달
    path: '/GX/createConference',
    name: 'createConference',
    component: () => import('@/components/modal/createConference.vue')
  },
  {
    // gx룸
    path: '/gx/conferences/:id',
    name: 'GxRoom',
    component: () => import('@/views/room/GxRoom.vue')
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
  },

  // ------------ PX 페이지 관련 ---------------
  {
    path: '/PX',
    component: () => import('@/views/px/PxView.vue'),
    redirect: '/PX/diaries',
    childeren: [
      {
        // 식단 다이어리
        path: 'diaries',
        name: 'pxDiaries',
        component: () => import('@/components/px/DietDiary.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
