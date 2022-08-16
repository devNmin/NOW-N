const HOST = 'http://127.0.0.1:8000'
// const HOST = 'http://i7b108.p.ssafy.io/:8000'

// const USERS = 'users/'

export default {
  accounts: {
    login: () => HOST + '/accounts/' + 'login/',
    signup: () => HOST + '/accounts/' + 'signup/',
    changePw: (userPk) => HOST + '/accounts/change_pw/' + `${userPk}/`
    // Token 으로 현재 user 판단
  },
  // 룸 정보
  rooms: {
    room: () => HOST + '/GX/conferences/',
    createRoom: () => HOST + '/GX/createconference/',
    articleList: (articleCategory) => HOST + `/community/${articleCategory}/`, // 1 전체 2 공지 3 자유 4 질문
    article: () => HOST + '/community/article/',
    articleDelete: (articleId) => HOST + '/community/article/' + `${articleId}/`
  },
  // 트레이너
  trainer: {
    // 그냥 트레이너 페이지
    list: () => HOST + '/trainer/select/',
    search: (nickname) => HOST + '/trainer/' + 'searchbynick/' + `${nickname}`,
    requestDetail: (coachPK) => HOST + '/trainer/select/' + `${coachPK}`,
    requestCounsel: (userPk, coachPk) => HOST + '/trainer/counsel/' + `${userPk}/` + `${coachPk}`,
    // 트레이너의 유저관리
    applyCounselting: (coachPK) => HOST + '/trainer/counsel/' + `${coachPK}`,
    applicantList: () => HOST + '/trainer/getrequestlist/',
    acceptCounselting: (userPk) => HOST + '/trainer/savecounsel/' + `${userPk}`,
    rejectCounselting: (userPk) => HOST + '/trainer/deleterequest/' + `${userPk}`,
    getmemberlist: (coachPk) => HOST + '/trainer/getmemberlist/' + `${coachPk}`,
    updateTrainer: (userPk) => HOST + '/trainer/modify/' + `${userPk}`,
    getCounselList: (anotherPk) => HOST + '/trainer/getmembercounsellist/' + `${anotherPk}`,
    getCounselDetail: (counselPk) => HOST + '/trainer/getmembercounsel/' + `${counselPk}`
  },
  // 프로필
  profiles: {
    doFollow: (anotherPk) => HOST + '/profiles/select/' + `${anotherPk}` + '/follow',
    followList: (userPk) => HOST + '/profiles/followlist/' + `${userPk}`,
    followRecommend: () => HOST + '/profiles/recommendlist',
    isFollow: (anotherPk) => HOST + '/profiles/checkfollow/' + `${anotherPk}`,
    // http://127.0.0.1:8000/profiles/select/1
    profiles: (userPk) => HOST + '/profiles/select/' + `${userPk}`,
    modify: (userPk) => HOST + '/profiles/modify/' + `${userPk}`
  },
  // px
  px: {
    dietList: (userPk) => HOST + '/PX/diaries/' + `${userPk}`,
    info: {
      coachInfo: (coachPk) => HOST + '/PX/mytrainer/' + `${coachPk}`,
      trainhistory: (coachPk) => HOST + '/PX/trainhistory/' + `${coachPk}`,
      counselhistory: (coachPk) => HOST + '/PX/counselhistory/' + `${coachPk}`,
      schedule: (coachPk) => HOST + '/PX/schedule/' + `${coachPk}`
    }
  }

}
