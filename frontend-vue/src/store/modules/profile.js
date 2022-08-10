export default {
  state: {
    UserInfo: {
      name: '뚱이.png',
      follower: '13',
      following: '155',
      profile_url: '',
      information: '#바나나 #코딩 #릴라고 #조는중',
      sex1: '남성',
      height1: '174.4',
      weight1: '85.5',
      goal1: '75.5',
      exercise: {
        Yoga: 3,
        Pilates: 4,
        FullBody: 5,
        Stretching: 1,
        Machine: 0,
        Etc: 2
      }
    }
  },
  getters: {
    currentUser: state => state.currentUser
  }
}
