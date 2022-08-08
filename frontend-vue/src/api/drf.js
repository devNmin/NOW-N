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
<<<<<<< HEAD
    CDRoom: () => HOST + '/GX/createconference/'
=======
    CDRoom: () => HOST + '/gx/room/'
  },
  trainer: {
    list: () => HOST + '/trainer/select/'
>>>>>>> 61ac4e27d651f06593c65175950513fc271b94c3
  }
}
