import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default {
  state: {
    dietList: [], // 해당 날짜 식단 리스트
    searchingLists: [],
    weightSeven: []
  },
  getters: {
    searchingLists: (state) => state.searchingLists,
    weightSeven: (state) => state.weightSeven
  },
  mutations: {
    // 식단 등록 시 리스트 갱신
    SET_SEARCH_LISTS: (state, searchingData) => { state.searchingLists = searchingData },
    SET_WEIGHT_LISTS: (state, weightSeven) => { state.weightSeven = weightSeven }
  },
  actions: {
    async getWeightDay ({ commit }, userPk) {
      await axios({
        url: drf.px.getWeightDay(),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        commit('SET_WEIGHT_LISTS', res.data)
      })
    },
    async getWeightWeek ({ commit }, userPk) {
      await axios({
        url: drf.px.getWeightWeek(),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        commit('SET_WEIGHT_LISTS', res.data)
        console.log(res.data)
      })
    },
    async getWeightMonth ({ commit }, userPk) {
      await axios({
        url: drf.px.getWeightMonth(),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        commit('SET_WEIGHT_LISTS', res.data)
      })
    },
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
    createDiet ({ commit }, DietInfo) {
      axios({
        // url: drf.px.createDiet(),
        url: 'http://127.0.0.1:8000/PX/creatediets/',
        method: 'POST',
        data: DietInfo,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log('createDiet', res.data)
          router.push({ name: 'pxDiaries' })
        }
        )
    },
    async searchDietName ({ commit }, name) {
      console.log('dietjs', name)
      // const test = '닭'
      const credentials = {
        name: name
      }
      await axios({
        // url: drf.px.searchDietName(),
        url: 'http://127.0.0.1:8000/PX/selectfoodbyname',
        method: 'post',
        data: credentials,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          // console.log('searchDietName', res.data)
          commit('SET_SEARCH_LISTS', res.data)
          // commit('SET_PROFILE', res.data)
        }
        ).catch(e => {
          console.log(e)
        }
        )
    },
    searchDietPk ({ commit }, foodPK) {
      axios({
        url: drf.px.searchDietPk(foodPK),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log('searchDietPk', res.data)
          // commit('SET_PROFILE', res.data)
        }
        )
    }
  }
}
