
export default {
  state: {
    listMode: true
  },
  getters: {
    listMode: (state) => state.listMode
  },
  mutations: {
    SET_LIST_MODE (state) { state.listMode = !state.listMode }
  },
  actions: {
  }
}
