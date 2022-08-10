import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    hideFollow: false,
    a: true
  },
  getters: {
    hideFollow: state => state.hideFollow
  },
  mutations: {
    SET_HIDE_FOLLOW: (state) => (state.hideFollow = !state.hideFollow),
    SET_A_MAKE: (state) => (state.a = !state.a)
  },
  actions: {
    hide ({ commit }) {
      commit('SET_HIDE_FOLLOW')
    },
    trainerList ({ commit }, data) {
      axios({
        url: drf.trainer.list(),
        method: 'get',
        data: data,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log(data)
          console.log(res)
          commit('SET_A_MAKE')
        })
    }
  }
}
