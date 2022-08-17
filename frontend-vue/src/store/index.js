import { createStore } from 'vuex'

import accounts from './modules/accounts'
import profile from './modules/profile'
import room from './modules/room'
import trainer from './modules/trainer'
import follow from './modules/follow'
import px from './modules/px'
import counsel from './modules/counsel'
import diet from './modules/diet'
export default createStore({
  modules: { accounts, profile, room, trainer, follow, px, counsel, diet }
})
