import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    dietList: [], // 해당 날짜 식단 리스트
    infomations: {
      coach: {},
      trainhistory: {},
      counselhistory: {},
      schedule: {}
    }
  },
  getters: {
    infomations: (state) => state.infomations
  },
  mutations: {
    // 해당 날짜 리스트 설정
    SET_DIET_LIST (state, dietList) {
      state.dietList = dietList
    },

    // 식단 등록 시 리스트 갱신
    CREATE_DDIET_INFO (state, dietInfo) {
      state.dietList.push(dietInfo)
    },

    // 룸 삭제
    DELETE_DIET_INFO (state, dietId) {
      state.dietList = state.dietList.filter(
        diet => diet.id !== dietId
      )
    },
    SET_INFOMATION_COACH (state, coach) { state.infomations.coach = coach },
    SET_INFOMATION_TR_HISTORY (state, trainhistory) { state.infomations.trainhistory = trainhistory },
    SET_INFOMATION_CS_HISTORY (state, counselhistory) { state.infomations.counselhistory = counselhistory },
    SET_INFOMATION_SCHEDULE (state, schedule) { state.infomations.schedule = schedule }
  },
  actions: {
    // 해당 날짜 식단 리스트 조회
    async getDietList ({ commit }, userPk, DietInfo) {
      const { data } = await axios({
        url: drf.px.dietList(userPk),
        method: 'POST',
        data: DietInfo,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
      commit('SET_DIET_LIST', data)
    },

    //  gx룸 삭제
    async deleteRoomInfo ({ commit }, roomId) {
      console.log(drf.rooms.room + `${roomId}/`)
      console.log(drf.trainer.requestDetail)
      await axios({
        url: drf.rooms.room + `${roomId}`,
        method: 'delete',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        commit('DELETE_ROOM_INFO', roomId)
      })
    },
    getCoachInfo ({ commit }, coachPK) {
      axios({
        url: drf.px.info.coachInfo(coachPK),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log(res.data)
          commit('SET_INFOMATION_COACH', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
      axios({
        url: drf.px.info.trainhistory(coachPK),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          commit('SET_INFOMATION_TR_HISTORY', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
      axios({
        url: drf.px.info.counselhistory(coachPK),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          commit('SET_INFOMATION_CS_HISTORY', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
      axios({
        url: drf.px.info.schedule(coachPK),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          commit('SET_INFOMATION_SCHEDULE', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    }
  }
}
