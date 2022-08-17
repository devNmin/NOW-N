import axios from 'axios'
import drf from '@/api/drf'
export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    myinfo: {}
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    profile: state => state.myinfo
  },

  mutations: {
    SET_PROFILE: (state, myinfo) => { state.myinfo = myinfo }
  },
  actions: {
    async profile ({ commit }, userPk) {
      await axios({
        url: drf.profiles.profiles(userPk),
        method: 'get',
        data: userPk,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        }
        )
    },
    async modify ({ commit }, credentials) {
      console.log('drf.profiles.modify(userPk)', localStorage.getItem('userPk'))
      console.log('drf.profilescredentials', credentials)

      await axios({
        url: drf.profiles.modify(localStorage.getItem('userPk')),
        method: 'put',
        data: credentials,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log('MODIFY_PROFILE', res.data)
          // commit('SET_PROFILE', res.data)
        }
        )
    }
  }
}
