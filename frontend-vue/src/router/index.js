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
    path: '/room/gx',
    name: 'gxroom',
    component: () => import('@/views/room/GxRoom.vue')
  },
  {
    // 식단 다이어리
    // component에 view파일로 넣으면 페이지가 안나와서 임시로 DietDiary.vue로 연결
    path: '/PT/diet/getcalorie',
    name: 'dietdiary',
    component: () => import('@/components/px/DietDiary.vue')
  },
  {
    // 코칭룸
    path: '/PT/onetoone/enterroom',
    name: 'coachingroom',
    component: () => import('@/components/px/CoachingRoom.vue')
  },
  {
    // 체중그래프
    path: '/PT/graph/date',
    name: 'weightgraph',
    component: () => import('@/components/px/WeightGraph.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
