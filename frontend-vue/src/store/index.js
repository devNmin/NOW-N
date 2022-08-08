import { createStore } from 'vuex'

import accounts from './modules/accounts'
import profile from './modules/profile'
import room from './modules/room'
<<<<<<< HEAD

export default createStore({
  modules: { accounts, profile, room }
=======
import trainer from './modules/trainer'

export default createStore({
  modules: { accounts, profile, room, trainer }
>>>>>>> 40211c0fcb6f4727e0b42da32e228e3dc9c89085
})
