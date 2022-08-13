import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSweetalert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'
import { initializeApp, getApp, getApps } from 'firebase/app'

import { SetupCalendar } from 'v-calendar'
import 'v-calendar/dist/style.css'

createApp(App).use(store).use(router).use(SetupCalendar).use(VueSweetalert2).mount('#app')

// 파이어베이스 Config
const firebaseConfig = {
  apiKey: 'AIzaSyCXHGs5yNTyHSLXwjHvj5w9TWwwyeCOdwA',
  authDomain: 'commonproject-nown.firebaseapp.com',
  projectId: 'commonproject-nown',
  storageBucket: 'commonproject-nown.appspot.com',
  messagingSenderId: '621411719258',
  appId: '1:621411719258:web:318e731b7981144b496063',
  measurementId: 'G-C728BSH6FK'
}

// 파이어베이스 앱 초기화/설정 (이미 초기화되어있으면 기존 설정 사용)
const app = !getApps().length ? initializeApp(firebaseConfig) : getApp()

// 사용할 기능들은 알아보기 쉽게 이름을 지은뒤 export 해서 필요한곳에 사용하자
export default app

window.Kakao.init('44e203a985e2bc845fbbde8390a4fc5b')
