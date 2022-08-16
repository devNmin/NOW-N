import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    hideFollow: false,
    followList: {},
    recommendList: {},
    isFollow: null,
    modalData: 0
  },
  getters: {
    hideFollow: state => state.hideFollow,
    followList: (state) => state.followList,
    recommendList: (state) => state.recommendList,
    isFollow: (state) => state.isFollow,
    modalData: (state) => state.modalData
  },
  mutations: {
    SET_HIDE_FOLLOW: (state) => (state.hideFollow = !state.hideFollow),
    SET_FOLLOW_LIST: (state, followList) => { state.followList = followList },
    SET_RECOMMEND_LIST: (state, recommendList) => { state.recommendList = recommendList },
    SET_IS_FOLLOW: (state, data) => { state.isFollow = data },
    SET_MODAL_DATA: (state, Data) => { state.modalData = Data }

  },
  actions: {
    hide ({ commit }) {
      commit('SET_HIDE_FOLLOW')
    },
    doFollow ({ commit }, anotherPK) {
      axios({
        url: drf.profiles.doFollow(anotherPK),
        method: 'post',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log('팔로우 되었습니다')
        }).catch(err => {
          console.error(err.response.data)
        })
    },
    followList ({ commit }, userPk) {
      axios({
        url: drf.profiles.followList(userPk),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          commit('SET_FOLLOW_LIST', res.data)
        }).catch(err => {
          console.error(err.response.data)
        })
    },
    recommendList ({ commit }) {
      axios({
        url: drf.profiles.followRecommend(),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          commit('SET_RECOMMEND_LIST', res.data)
        }).catch(err => {
          console.error(err.response.data)
        })
    },
    isFollow ({ commit }, anotherPk) {
      axios({
        url: drf.profiles.isFollow(anotherPk),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log('1')
          console.log(res.data.value)
          console.log('2')
          commit('SET_IS_FOLLOW', res.data.value)
        }).catch(err => {
          console.error(err.response.data)
        })
    }
  }
}
