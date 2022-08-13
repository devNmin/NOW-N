import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    hideFollow: false,
    trainerList: {},
    trainerListCount: 0,
    currentTrainerPk: localStorage.getItem('coachPk') || '',
    currentTrainer: {},
    applyStamp: false
  },
  getters: {
    hideFollow: state => state.hideFollow,
    trainerList: state => state.trainerList,
    trainerListCount: state => state.trainerListCount,
    currentTrainerPk: state => state.currentTrainerPk,
    currentTrainer: state => state.currentTrainer,
    applyStamp: state => state.applyStamp
  },
  mutations: {
    SET_HIDE_FOLLOW: (state) => (state.hideFollow = !state.hideFollow),
    SET_TRAINER_LIST: (state, trainerList) => (state.trainerList = trainerList),
    SET_TRAINER_LIST_COUNT: (state, trainerListCount) => (state.trainerListCount = trainerListCount),
    SET_CURRENT_TRAINER_PK: (state, currentTrainerPk) => (state.currentTrainerPk = currentTrainerPk),
    SET_CURRENT_TRAINER: (state, currentTrainer) => (state.currentTrainer = currentTrainer),
    SET_APPLY_STAMP: (state, applyStamp) => (state.applyStamp = applyStamp)
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
          commit('SET_TRAINER_LIST_COUNT', res.data.Trainer_count)
          commit('SET_TRAINER_LIST', res.data.Trainer_List)
        })
    },
    trainerSearch ({ commit }, nickname) {
      axios({
        url: drf.trainer.search(nickname),
        method: 'get',
        data: nickname,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          commit('SET_TRAINER_LIST', res.data)
        })
    },
    requestTrainerDetail ({ commit }, coachPk) {
      axios({
        url: drf.trainer.requestDetail(coachPk),
        method: 'get',
        data: coachPk,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          commit('SET_CURRENT_TRAINER_PK', coachPk)
          commit('SET_CURRENT_TRAINER', res.data)
          localStorage.setItem('coachPk', coachPk)
        })
    },
    requestAdvice ({ commit, getters }, context) {
      const userPk = getters.currentUserPk
      const coachPk = getters.currentTrainerPk
      commit('SET_APPLY_STAMP', true)
      axios({
        url: drf.trainer.requestCounsel(userPk, coachPk),
        method: 'post',
        data: context.applyData,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          commit('SET_APPLY_STAMP', true)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    }
  }
}
