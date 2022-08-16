import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    listMode: true,
    applicantList: {},
    clientList: {}
  },
  getters: {
    listMode: (state) => state.listMode,
    applicantList: (state) => state.applicantList,
    clientList: (state) => state.clientList
  },
  mutations: {
    SET_LIST_MODE: (state) => { state.listMode = !state.listMode },
    SET_APPLICANT_LIST: (state, applicantList) => { state.applicantList = applicantList },
    SET_CLIENT_LIST: (state, clientList) => { state.clientList = clientList }
  },
  actions: {
    // 상담신청
    applyCounselting ({ commit }, coachPK) {
      axios({
        url: drf.trainer.applyCounselting(coachPK),
        method: 'post',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log('상담신청 되었습니다.')
        }).catch(err => {
          console.error(err.response.data)
        })
    },
    // 신청자 목록
    getApplycantList ({ commit }) {
      axios({
        url: drf.trainer.applicantList(),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log(res.data)
          commit('SET_APPLICANT_LIST', res.data)
        }).catch(err => {
          console.error(err.response.data)
        })
    },
    // 트레이닝 멤버 목록
    getClientList ({ commit }, coachPK) {
      console.log('adf')
      axios({
        url: drf.trainer.getmemberlist(coachPK),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log(res.data)
          commit('SET_CLIENT_LIST', res.data)
        }).catch(err => {
          console.error(err.response.data)
        })
    },
    // 상담 거절
    rejectCounselting ({ commit, dispatch }, userPk) {
      console.log('메렁')
      axios({
        url: drf.trainer.rejectCounselting(userPk),
        method: 'DELETE',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log(res.data)
          dispatch('getApplycantList')
        }).catch(err => {
          console.error(err.response.data)
        })
    },
    // 상담 수락 및 상담 내역 제출
    acceptCounselting ({ commit }, data) {
      const userPk = data[1]
      console.log(data[1])
      axios({
        url: drf.trainer.acceptCounselting(userPk),
        method: 'POST',
        data: data[0],
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log(res)
          localStorage.removeItem('applicantUserPk')
          router.push({ name: 'home' })
        }).catch(err => {
          console.error(err.response.data)
        })
    }
  }
}
