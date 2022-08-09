import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    currentUser: {},
    profile: {},
    authError: null,
    reduplication: false,
    accessToken: localStorage.getItem('accessToken') || '',
    refreshToken: localStorage.getItem('refreshToken') || ''
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Bearer ${state.accessToken}` }),
    loginViewCase: state => state.loginViewCase,
    getAccessToken: state => state.accessToken,
    getRefreshToken: state => state.refreshToken,
    getToken (state) {
      const accessToken = state.accessToken
      const refreshToken = state.refreshToken
      return {
        accessToken,
        refreshToken
      }
    }
  },

  mutations: {
    SET_ACCESSTOKEN: (state, accessToken) => { state.accessToken = accessToken },
    SET_REFRESHTOKEN: (state, refreshToken) => { state.refreshToken = refreshToken },
    SET_CURRENT_USER: (state, user) => { state.currentUser = user },
    // SET_PROFILE: (state, profile) => state.profile = profile,
    SET_REDUPLICATION (state, redup) {
      state.reduplication = redup
    },
    SET_AUTH_ERROR (state, error) {
      state.authError = error
    }
  },
  actions: {
    saveToken ({ commit }, Token) {
      /*
            state.token 추가
            localStorage에 token 추가
            */
      commit('SET_ACCESSTOKEN', Token.accessToken)
      commit('SET_REFRESHTOKEN', Token.refreshToken)
      localStorage.setItem('accessToken', Token.accessToken)
      localStorage.setItem('refreshToken', Token.refreshToken)
    },

    logout ({ commit }) {
      /*
            localStorage에 token 추가
            */
      // 토큰삭제
      router.push({ name: 'home' })
      commit('SET_ACCESSTOKEN', '')
      commit('SET_REFRESHTOKEN', '')
      localStorage.setItem('accessToken', '')
      localStorage.setItem('refreshToken', '')
    },

    login ({ commit, dispatch, getters }, credentials) {
      /*
            POST: 사용자 입력정보를 login URL로 보내기
              성공하면
                응답 토큰 저장
                현재 사용자 정보 받기
                메인 페이지(ArticleListView)로 이동
              실패하면
                에러 메시지 표시
            */
      if (credentials.username === '') {
        credentials.username = '#########'
      }
      if (credentials.password === '') {
        credentials.password = 'qwerty1234'
      }
      console.log(credentials)
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const accessToken = res.data.token.access
          const refreshToken = res.data.token.refresh
          const Token = {
            accessToken,
            refreshToken
          }
          dispatch('saveToken', Token)
          commit('SET_CURRENT_USER', credentials)
          console.log(getters.currentUser)
          // dispatch('fetchCurrentUser')
          router.push({ name: 'home' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    signup ({ commit, dispatch }, credentials) {
      // 회원가입
      // 1. 프레쉬 토큰과 액세스 토큰저장
      console.log(credentials)
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const accessToken = res.data.token.access
          const refreshToken = res.data.token.refresh
          const Token = {
            accessToken,
            refreshToken
          }
          dispatch('saveToken', Token)
          // dispatch('fetchCurrentUser')
          router.push({ name: 'home' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    }
  }
}
