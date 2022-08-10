import { createStore } from 'vuex'

import accounts from './modules/accounts'
import profile from './modules/profile'
<<<<<<< HEAD

export default createStore({
  modules: { accounts, profile }
=======
import room from './modules/room'
import trainer from './modules/trainer'

export default createStore({
  modules: { accounts, profile, room, trainer }
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
})
