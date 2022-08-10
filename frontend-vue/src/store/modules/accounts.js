import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
<<<<<<< HEAD

=======
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
<<<<<<< HEAD
    token: localStorage.getItem('token') || '',
    currentUser: {},
    profile: {},
    authError: null,
    reduplication: false // 중복체크
=======
    currentUser: {},
    profile: {},
    authError: null,
    reduplication: false,
    accessToken: localStorage.getItem('accessToken') || '',
    refreshToken: localStorage.getItem('refreshToken') || ''
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
<<<<<<< HEAD
    authHeader: state => ({ Authorization: `Token ${state.token}` }),
    loginViewCase: state => state.loginViewCase

  },

  mutations: {
    // SET_TOKEN: (state, token) => state.token = token,
    // SET_CURRENT_USER: (state, user) => state.currentUser = user,
=======
    authHeader: state => ({ Authorization: `Bearer ${state.accessToken}` }),
    loginViewCase: state => state.loginViewCase,
    TokenHeader: state => ({ Authorization: `JWT ${state.accessToken}` })
  },

  mutations: {
    SET_ACCESSTOKEN: (state, accessToken) => { state.accessToken = accessToken },
    SET_REFRESHTOKEN: (state, refreshToken) => { state.refreshToken = refreshToken },
    SET_CURRENT_USER: (state, user) => { state.currentUser = user },
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
    // SET_PROFILE: (state, profile) => state.profile = profile,
    SET_REDUPLICATION (state, redup) {
      state.reduplication = redup
    },
    SET_AUTH_ERROR (state, error) {
      state.authError = error
    }
  },
<<<<<<< HEAD

  actions: {
    saveToken ({ commit }, token) {
=======
  actions: {
    saveToken ({ commit }, Token) {
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
      /*
            state.token 추가
            localStorage에 token 추가
            */
<<<<<<< HEAD
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken ({ commit }) {
      /*
            state.token 삭제
            localStorage에 token 추가
            */
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    login ({ commit, dispatch, state }, credentials) {
=======
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
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
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
<<<<<<< HEAD
      credentials.face_vector = state.faceVector
=======
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
      console.log(credentials)
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
<<<<<<< HEAD
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'articles' })
=======
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
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
<<<<<<< HEAD
    signup ({ commit, dispatch }, credentials) {
=======

    signup ({ commit, dispatch }, credentials) {
      // 회원가입
      // 1. 프레쉬 토큰과 액세스 토큰저장
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
      console.log(credentials)
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
<<<<<<< HEAD
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'articles' })
=======
          const accessToken = res.data.token.access
          const refreshToken = res.data.token.refresh
          const Token = {
            accessToken,
            refreshToken
          }
          dispatch('saveToken', Token)
          // dispatch('fetchCurrentUser')
          router.push({ name: 'home' })
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
<<<<<<< HEAD
    },

    logout ({ getters, dispatch }) {
      /*
            POST: token을 logout URL로 보내기
              성공하면
                토큰 삭제
                사용자 알람
                LoginView로 이동
              실패하면
                에러 메시지 표시
            */
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        // data: {},
        headers: getters.authHeader
      })
        .then(() => {
          dispatch('removeToken')
          alert('성공적으로 logout!')
          router.push({ name: 'login' })
        })
        .error(err => {
          console.error(err.response)
        })
    },

    fetchCurrentUser ({ commit, getters, dispatch }) {
      /*
            GET: 사용자가 로그인 했다면(토큰이 있다면)
              currentUserInfo URL로 요청보내기
                성공하면
                  state.cuurentUser에 저장
                실패하면(토큰이 잘못되었다면)
                  기존 토큰 삭제
                  LoginView로 이동
            */
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader
        })
          .then(res => commit('SET_CURRENT_USER', res.data))
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchProfile ({ commit, getters }, { username }) {
      /*
            GET: profile URL로 요청보내기
              성공하면
                state.profile에 저장
            */
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
=======
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
    }
  }
}
