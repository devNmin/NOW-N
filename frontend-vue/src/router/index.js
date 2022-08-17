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
    // 트레이너 정보변경
    path: '/updateTrainer',
    name: 'update',
    component: () => import('@/views/user/UpdateTrainer.vue')
  },

  // ------------ GX 페이지 Start ---------------
  {
    // G.X 메인페이지
    path: '/GX',
    component: () => import('@/views/gx/GroupXerciseView.vue'),
    redirect: '/GX/conferences',
    children: [
      {
        // gx룸
        path: 'conferences',
        name: 'gxConferences',
        component: () => import('@/components/gx/GroupXercise.vue')
      },
      {
        // GX 커뮤니티
        path: 'community',
        name: 'GXcommunity',
        component: () => import('@/components/gx/GXcommunity.vue')
      },
      {
        // GX 커뮤니티
        path: 'createArticle',
        name: 'GXCreateArticle',
        component: () => import('@/components/gx/GXCreateArticle.vue')
      }
    ]
  },
  {
    // gx 방 생성모달
    path: '/GX/createConference',
    name: 'createConference',
    component: () => import('@/components/modal/createConference.vue')
  },
  {
    // gx룸
    path: '/GX/conferences/:conference_id',
    name: 'GxRoom',
    props: true,
    component: () => import('@/views/room/GxRoom.vue')
  },
  // ------------ GX 페이지 End ---------------
  // ------------ 트레이너 페이지 start ----------
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
  // ------------ 트레이너 페이지 end ----------
  // ------------ PX 페이지 Start ---------------
  {
    path: '/PX',
    component: () => import('@/views/px/PxView.vue'),
    redirect: '/px/diaries',
    children: [
      {
        // 식단 다이어리
        path: 'diaries',
        name: 'pxDiaries',
        component: () => import('@/components/px/DietDiary.vue')
      },
      {
        // 체중 그래프
        path: 'graph',
        name: 'pxGraph',
        component: () => import('@/components/px/WeightGraph.vue')
      },
      {
        // 1:1 코칭룸
        path: 'coaching',
        name: 'pxCoaching',
        component: () => import('@/components/px/CoachingRoom.vue')
      }
    ]
  },
  {
    // px 식단 등록 모달
    path: '/px/createDiet',
    name: 'createDiet',
    component: () => import('@/components/modal/createDiet.vue')
  },
  {
    // px룸
    path: '/px/personalroom',
    name: 'pxPersonal',
    component: () => import('@/views/room/PxRoom.vue')
  },
  {
    // counsel 유저 리스트
    path: '/counselting',
    name: 'counselting',
    component: () => import('@/views/counselting/CounseltingClientView.vue')
  },
  // ------------ PX 페이지 End ---------------
  // ------------ counselting 페이지 start ----------
  {
    // counsel 유저 리스트
    path: '/counseltingApplicant',
    name: 'counseltingApplicant',
    component: () => import('@/views/counselting/CounseltingApplicantView.vue')
  },
  {
    // counsel 유저 리스트
    path: '/counseltingClient',
    name: 'counseltingClient',
    component: () => import('@/views/counselting/CounseltingClientView.vue')
  },
  {
    // counsel 페이지
    path: '/counselting/apply',
    name: 'counseltingApply',
    component: () => import('@/components/counselting/applicant/CounseltingApplyRoom.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
