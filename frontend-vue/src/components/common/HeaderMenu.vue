<template>
    <div >
      <div class='navcontent'>
        <div class="navLeft" style="display: flex; justify-content: flex-start;">
        <a href="/">
          <img src="@\assets\Logo2.png" alt="Logo2.png"  height="35">
        </a>
        <router-link class='headerItem'
          v-for="item in leftItems" :key="item.link" :to="item.link">
          <img :src="item.icon" alt=""> {{item.name}}
        </router-link>
        </div>
        <div class="navRight">
          <template v-if="isLoggedIn">
            <router-link class='headerItem' :to="LogInItems.link">
              <img :src="LogInItems.icon" alt=""/> {{LogInItems.name}}
            </router-link>
            <div class="logout-btn" @click="logout">Logout</div>
          </template>

          <template v-else>
            <router-link class='headerItem'
              v-for="item in rightItems" :key="item.link" :to="item.link">
              <img :src="item.icon" alt=""/> {{item.name}}
            </router-link>
          </template>
        </div>
      </div>
    </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  setup () {
    const store = useStore()

    const isLoggedIn = computed(() => {
      return store.getters.isLoggedIn
    })

    const leftItems = [
      { name: 'G . X', link: '/GX', icon: '@\\assets\\Logo2.png' },
      { name: 'P . X', link: '/px', icon: '@\\assets\\Logo2.png' },
      { name: 'Trainer', link: '/trainer', icon: '@\\assets\\Logo2.png' }
    ]
    const rightItems = [
      { name: 'Login', link: '/login', icon: '@/assets/Logo2.png' }, // require('@/assets/Logo2.png')
      { name: 'signup', link: '/signUp', icon: '@\\assets\\Logo2.png' }
    ]
    const LogInItems = {
      name: 'Profile',
      link: '/profiles'
    }

    function logout () {
      store.dispatch('logout')
    }

    return { isLoggedIn, leftItems, rightItems, LogInItems, logout }
  }
}
</script>

<style scoped>
.headerItem{
  display:flex;
  align-items: center;
  text-decoration: none;
  font-weight: bolder;
  font-size: 1.3rem;
  color: #6DCEF5;
  padding: 0 10px;
  /* color: black; */
}

.navLeft{
  display: flex;
  justify-content: flex-end;
  gap: 20px;
}
.navRight{
  display: flex;
  justify-content: flex-end;
  gap: 20px;
}

.navcontent{
    display: flex;
    height: 40px;
    padding: 22px 64px;
    font-size: 1.1em;
    margin-bottom: 2px;
    justify-content: space-between;
    /* background: linear-gradient(lightCyan, skyBlue, #6DCEF5); */
    border-bottom:1px skyBlue;
    box-shadow: 0px 2px 4px #6DCEF5;
    align-items: center;
    /* background-color: #6DCEF5; */
}

.headerItem:hover{
  background-color: #6DCEF5;
  border-radius: 10px;
  color: white;
}

.headerItem:active{
  color: #4BB2FF;
}

.headerItem.router-link-active {
  border-bottom: 2px solid #4BB2FF;
  color: #4BB2FF;
}

.logout-btn {
  cursor: pointer;
}
</style>
