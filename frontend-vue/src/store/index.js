import { createStore } from 'vuex'

import accounts from './modules/accounts'
import profile from './modules/profile'
import room from './modules/room'
import trainer from './modules/trainer'
import follow from './modules/follow'
import counsel from './modules/counsel'
export default createStore({
  modules: { accounts, profile, room, trainer, follow, counsel }
})
