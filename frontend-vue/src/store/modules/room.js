import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    roomList: [], // 모든 룸 리스트
    roomInfo: [] // 현재 룸
  },
  getters: {
  },
  mutations: {
    // 모든 룸 리스트를 State에 저장
    SET_ROOM_LIST (state, roomList) {
      state.roomList = roomList
    },

    // 룸 생성시 리스트, 현재 룸을 State에 저장
    CREATE_ROOM_INFO (state, roomInfo) {
      state.roomList.push(roomInfo)
      state.roomInfo = roomInfo
    },

    // 룸 삭제
    DELETE_ROOM_INFO (state, roomId) {
      state.roomList = state.roomList.filter(
        room => room.id !== roomId
      )
    }
  },
  actions: {
    // gx룸 상세 조회
    async getRoomInfo ({ commit }, roomId) {
      const { data } = await axios({
        url: drf.rooms.room() + `${roomId}`,
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
      commit('SET_ROOM_INFO', data)
    },

    // gx룸 리스트 조회
    async getRoomList ({ commit }) {
      const { data } = await axios({
        url: drf.rooms.room(),
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      })
      commit('SET_ROOM_LIST', data)
    },

    // gx룸 생성
    async createRoomInfo ({ commit }, roomInfo) {
      await axios({
        url: drf.rooms.createRoom(),
        method: 'POST',
        data: roomInfo,
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        commit('CREATE_ROOM_INFO', res.data)
      })
        .catch(err => {
          console.error(err.response.data)
        })
    },

    //  gx룸 삭제
    async deleteRoomInfo ({ commit }, roomId) {
      await axios({
        url: drf.rooms.room() + roomId + '/',
        method: 'delete',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        console.log('삭제 완료 로직')
        commit('DELETE_ROOM_INFO', roomId)
        router.push({ name: 'gxConferences' })
      })
        .catch(err => {
          console.error(err.response.data)
        })
    }
  }
}
