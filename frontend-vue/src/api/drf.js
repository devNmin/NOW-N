const HOST = 'http://127.0.0.1:8000'

// const USERS = 'users/'

export default {
  accounts: {
    login: () => HOST + '/accounts/' + 'login/',
    signup: () => HOST + '/accounts/' + 'signup/'
    // Token 으로 현재 user 판단
  },
  rooms: {
    roomList: () => HOST + '/gx/getRoomlist/',
    roomInfo: () => HOST + '/gx/getRoomInfo/',
    createRoom: () => HOST + '/GX/createconference/'
  },
  trainer: {
    list: () => HOST + '/trainer/select/',
    search: (nickname) => HOST + '/trainer/' + `${nickname}/`,
    request: (userPk, coachPk) => HOST + '/trainer/' + `${userPk}/` + `${coachPk}/`
  }
}
