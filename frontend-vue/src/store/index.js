import { createStore } from 'vuex'
import axios from 'axios'
import router from '@/router'

import accounts from './modules/accounts'

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
    SET_AUTH_ERROR: (state, error) => { state.authError = error }
  },
  actions: {
    saveToken ({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },
    removeToken ({ commit }) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },
    signup ({ commit, dispatch }, credentials) {
      console.log('메렁')
      console.log(credentials)
      axios({
        url: 'http://127.0.0.1:8000/accounts/signup/',
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'articles' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    fetchCurrentUser ({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: 'http://127.0.0.1:8000/accounts/current/',
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
    }
  },
  modules: {
  }
})
