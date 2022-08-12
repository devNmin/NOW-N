// import axios from 'axios'
// import drf from '@/api/drf'

// export default {
//   state: {
//   },
//   getters: {
//   },
//   mutations: {
//   },
//   actions: {
//     followList ({ commit }) {
//       axios({
//         url: drf.trainer.requestDetail(coachPk),
//         method: 'get',
//         data: coachPk,
//         headers: { Authorization: 'JWT ' + localStorage.accessToken }
//       })
//         .then(res => {
//           commit('SET_CURRENT_TRAINER_PK', coachPk)
//           commit('SET_CURRENT_TRAINER', res.data)
//           localStorage.setItem('coachPk', coachPk)
//         })
//   }
// }
