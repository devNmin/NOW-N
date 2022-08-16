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
    createRoom: () => HOST + '/GX/createconference/',
    articleList: (articleCategory) => HOST + `/community/${articleCategory}/`, // 1 전체 2 공지 3 자유 4 질문
    article: () => HOST + '/community/article/',
    articleDelete: (articleId) => HOST + '/community/article/' + `${articleId}/`
  },

  trainer: {
    list: () => HOST + '/trainer/select/',
    search: (nickname) => HOST + '/trainer/' + 'searchbynick/' + `${nickname}`,
    requestDetail: (coachPK) => HOST + '/trainer/select/' + `${coachPK}`,
    requestCounsel: (userPk, coachPk) => HOST + '/trainer/counsel/' + `${userPk}/` + `${coachPk}`
  },

  profiles: {
    // http://127.0.0.1:8000/profiles/select/1
    profiles: (userPk) => HOST + '/profiles/select/' + `${userPk}`,
    modify: (userPk) => HOST + '/profiles/modify/' + `${userPk}`
  },
  px: {
    dietList: (userPk) => HOST + '/PX/diaries/' + `${userPk}`,
    trainerId: (userPk) => HOST + '/PX/trainer/' + `${userPk}`
  }

}
