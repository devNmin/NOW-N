import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    dietList: [] // 해당 날짜 식단 리스트
  },
  getters: {
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
    }
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
    }
  }
}
