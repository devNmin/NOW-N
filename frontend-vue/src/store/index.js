import { createStore } from 'vuex'

import accounts from './modules/accounts'
import profile from './modules/profile'

export default createStore({
  modules: { accounts, profile }
})
