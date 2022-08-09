// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    roomList: [], // 모든 룸 리스트
    roomInfo: {} // 현재 룸
  },
  getters: {
  },
  mutations: {
    // 현재 룸 번호 State에 저장
    SET_ROOM_INFO (state, roomId) {
      state.roomId = roomId
    },

    // 모든 룸 리스트를 State에 저장
    SET_ROOM_LIST (state, roomList) {
      state.roomList = roomList
    },

    // 모든 룸 생성
    CREATE_ROOM_INFO (state, roomInfo) {
      state.roomList.push(roomInfo)
    },

    // 룸 삭제
    DELETE_ROOM_INFO (state, roomInfo) {
      state.roomList = state.roomList.filter(
        room => room.roomId !== roomInfo
      )
    }
  },
  actions: {
    // gx룸 상세 조회
    async getRoomInfo ({ commit }, roomId) {
      const { data } = await axios({
        url: drf.rooms.roomInfo() + `${roomId}`,
        method: 'get'
      })
      commit('SET_ROOM_INFO', data)
    },

    // gx룸 리스트 조회
    async getRoomList ({ commit, getters }) {
      const { data } = await axios({
        url: drf.rooms.roomList(),
        method: 'get',
        headers: getters.getToken.accessToken
      })
      commit('SET_ROOM_LIST', data)
    },

    // gx룸 생성
    async createRoomInfo ({ commit }, roomInfo) {
      try {
        await axios({
          url: drf.rooms.createRoom(),
          method: 'post',
          data: roomInfo,
          headers: { Authorization: 'JWT' + localStorage.accessToken }
        })
      } catch (e) {
        console.log('에러')
        console.log(e)
      }
      commit('CREATE_ROOM_INFO', roomInfo)
    },

    //  gx룸 삭제
    async deleteRoomInfo ({ commit }, roomId) {
      await axios({
        url: drf.rooms.CDRoom(),
        method: 'delete'
      })
      commit('DELETE_ROOM_INFO', roomId)
    }
  }
}
