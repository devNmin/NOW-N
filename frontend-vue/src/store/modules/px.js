import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    dietList: [], // 해당 날짜 식단 리스트
    user_trainer: [], // 현재 유저의 트레이너
    weightList: [] // 현재 유저의 weight data
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

    // 현재 유저의 트레이너 저장
    SET_USER_TRAINER (state, info) {
      state.user_trainer = info
    },

    // 현재 유저의 weight 저장
    SET_USER_WEIGHT (state, weightList) {
      state.weightList = weightList
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

    // 코치 정보 조회
    getTrainerId ({ commit }, userPk) {
      axios({
        url: drf.px.trainerId(userPk),
        method: 'get',
        data: userPk,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        axios({
          url: drf.px.trainerInfo(res.data),
          method: 'get',
          data: res.data,
          headers: { Authorization: 'JWT ' + localStorage.accessToken }
        }).then(info => {
          commit('SET_USER_TRAINER', info)
        })
      })
    },

    // 체중 그래프 데이터 조회
    getWeight ({ commit }, userPk) {
      axios({
        url: drf.px.weight(userPk),
        method: 'get',
        data: userPk,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        commit('SET_USER_WEIGHT', res.data)
      })
    }
  }
}
