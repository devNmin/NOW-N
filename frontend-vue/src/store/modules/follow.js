import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    followList ({ commit, getters }) {
      const userPk = getters.currentUserPk
      axios({
        url: drf.trainer.requestDetail(userPk),
        method: 'get',
        data: userPk,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
        .then(res => {
          console.log(res)
        })
    }
  }
}
