import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    hideFollow: false,
    trainerList: {}
  },
  getters: {
    hideFollow: state => state.hideFollow,
    trainerList: state => state.trainerList
  },
  mutations: {
    SET_HIDE_FOLLOW: (state) => (state.hideFollow = !state.hideFollow),
    SET_TRAINER_LIST: (state, trainerList) => (state.trainerList = trainerList)
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
        })
    },
    trainerSearch ({ commit }, nickname) {
      axios({
        url: drf.trainer.list(),
        method: 'get',
        data: nickname,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log(res)
          commit('SET_NICK_NAME_SEARCH_USER')
        })
    },
    requestAdvice ({ commit }, { userPk, coachPk, context }) {
      axios({
        url: drf.trainer.request(userPk, coachPk),
        method: 'post',
        data: context,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log(res)
          commit('SET_NICK_NAME_SEARCH_USER')
        })
    }
  }
}
