export default {
  state: {
    hideFollow: false
  },
  getters: {
    hideFollow: state => state.hideFollow
  },
  mutations: {
    SET_HIDE_FOLLOW: (state) => (state.hideFollow = !state.hideFollow)
  },
  actions: {
    hide ({ commit }) {
      commit('SET_HIDE_FOLLOW')
    }
  }
}
