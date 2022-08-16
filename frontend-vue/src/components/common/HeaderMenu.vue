<template>
    <div >
      <div class='navcontent'>
        <div class="navLeft" style="display: flex; justify-content: flex-start; align-items: center;">
          <a href="/" class="">
            <img src="@\assets\Logo2.png" href="/" alt="Logo2.png"  height="35">
          </a>
        <div class="dropdown">
          <router-link class="dropbtn headerItem" to="/GX/conferences">
            G . X
            </router-link>
          <div class="dropdown-content">
            <router-link class='' to="/GX/conferences">
            G.X Room
            </router-link>
            <router-link class='' to="/GX/community">
            community
            </router-link>
          </div>
        </div>
        <div class="dropdown">
          <router-link class="dropbtn headerItem" to="/px/diaries">
            P . X
            </router-link>
          <div class="dropdown-content">
            <router-link class='' to="/px/diaries">
            식단 다이어리
            </router-link>
            <router-link class='' to="/px/graph">
            체중 그래프
            </router-link>
            <router-link class='' to="/px/coaching">
            코칭 룸
            </router-link>
          </div>
        </div>
        <div class="dropdown">
            <router-link class='dropbtn headerItem' to="/trainer">
              Trainer
            </router-link>
          </div>
        <div class="dropdown">
        <router-link class="dropbtn headerItem" to="/counseltingApplicant">
          Consulting
          </router-link>
        <div class="dropdown-content">
          <router-link class='' to="/counseltingApplicant">
          Applicant
          </router-link>
          <router-link class='' to="/counseltingClient">
          Client
          </router-link>
          <router-link class='' to="/updateTrainer">
          Updata
          </router-link>
        </div>
      </div>
        </div>
        <div class="navRight">
          <template v-if="isLoggedIn">
            <router-link class='headerItem' :to="LogInItems.link">
              <img src="" alt=""/> {{LogInItems.name}}
              <!-- <img :src="LogInItems.icon" alt=""/> {{LogInItems.name}} -->
            </router-link>
            <div class="logout-btn headerItem" @click="logout">Logout</div>
          </template>

          <template v-else>
            <router-link class='headerItem'
              v-for="item in rightItems" :key="item.link" :to="item.link">
              <!-- <img :src="item.icon" alt=""/> {{item.name}} -->
              <img src="" alt=""/> {{item.name}}
            </router-link>
          </template>
        </div>
      </div>
    </div>
</template>

<script>
import { computed, inject } from 'vue'
import { useStore } from 'vuex'
export default {
  components: {
  },
  setup () {
    const swal = inject('$swal')
    const store = useStore()

    const isLoggedIn = computed(() => {
      return store.getters.isLoggedIn
    })

    const rightItems = [
      { name: 'Login', link: '/login', icon: '@/assets/Logo2.png' }, // require('@/assets/Logo2.png')
      { name: 'signup', link: '/signUp', icon: '@\\assets\\Logo2.png' }
    ]
    const LogInItems = {
      name: 'Profile',
      link: '/profiles'
    }

    function logout () {
      swal({
        text: '로그아웃 되었습니다.',
        type: 'warning',
        timer: 1500,
        customClass: 'sweet-size',
        confirmButtonClass: 'btn-danger',
        showConfirmButton: false
      })
      store.dispatch('logout')
    }

    return { isLoggedIn, rightItems, LogInItems, logout }
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
.dropbtn {
  /* dropdown */
  padding: 16px;
  font-size: 1.3rem;
  border: none;
}
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown:hover .dropdown-content {display: block;}

</style>
