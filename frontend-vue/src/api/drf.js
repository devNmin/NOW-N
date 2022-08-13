const HOST = 'http://127.0.0.1:8000'
// const HOST = 'http://i7b108.p.ssafy.io/:8000'

// const USERS = 'users/'

export default {
  accounts: {
    login: () => HOST + '/accounts/' + 'login/',
    signup: () => HOST + '/accounts/' + 'signup/'
    // Token 으로 현재 user 판단
  },
  rooms: {
    room: () => HOST + '/GX/conferences/',
    createRoom: () => HOST + '/GX/createconference/'
  },
  trainer: {
    list: () => HOST + '/trainer/select/',
    search: (nickname) => HOST + '/trainer/' + 'searchbynick/' + `${nickname}`,
    requestDetail: (coachPK) => HOST + '/trainer/select/' + `${coachPK}`,
    requestCounsel: (userPk, coachPk) => HOST + '/trainer/counsel/' + `${userPk}/` + `${coachPk}`
  },
  profiels: {
    profiels: (userPk) => HOST + '/profiles/followlist/' + `${userPk}`
  },
  px: {
    dietList: (userPk) => HOST + '/PX/diaries/' + `${userPk}`
  }
}
