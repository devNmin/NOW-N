import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

createApp(App).use(store).use(router).mount('#app')
window.Kakao.init('44e203a985e2bc845fbbde8390a4fc5b')
