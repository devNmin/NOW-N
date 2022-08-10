<template>
    <div >
      <div class='navcontent'>
        <div class="navLeft" style="display: flex; justify-content: flex-start;">
        <a href="/">
          <img src="@\assets\Logo2.png" alt="Logo2.png"  height="40">
        </a>
        <router-link class='headerItem'
          v-for="item in leftItems" :key="item.link" :to="item.link">
          <img :src="item.icon" alt=""> {{item.name}}
        </router-link>
        </div>
        <div class="navRight">
          <router-link class='headerItem'
          v-for="item in rightItems" :key="item.link" :to="item.link">
          <img :src="item.icon" alt=""> {{item.name}}
        </router-link>
        </div>
      </div>
    </div>
</template>

<script>
// @\assets\Logo2.png"
export default {
  setup () {
<<<<<<< HEAD
    const commonItems = [
      { name: 'gx', link: '/GX' },
      { name: 'pt', link: '/pt' },
      { name: '트레이너', link: '/trainer' },
      { name: '로그인', link: '/login' }
=======
    const leftItems = [
      { name: 'G . X', link: '/GX', icon: '@\\assets\\Logo2.png' },
      { name: 'P . X', link: '/px', icon: '@\\assets\\Logo2.png' },
      { name: 'Trainer', link: '/trainer', icon: '@\\assets\\Logo2.png' }
    ]
    const rightItems = [
      { name: 'Login', link: '/login', icon: '@\\assets\\Logo2.png' },
      { name: 'signup', link: '/signUp', icon: '@\\assets\\Logo2.png' }
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
    ]

    return { leftItems, rightItems }
  }
}
</script>

<style scoped>
.headerItem{
  text-decoration: none;
  font-weight: bolder;
  font-size: 1.3rem;
  color: #6DCEF5;
  /* color: black; */
}

.navLeft{
  display: flex;
  justify-content: flex-end;
  gap: 32px;
}
.navRight{
  display: flex;
  justify-content: flex-end;
  gap: 32px;
}

.navcontent{
    display: flex;
    height: 1rem;
    padding: 32px 64px;
    font-size: 1.1em;
    margin-bottom: 2px;
    justify-content: space-between;
    /* background: linear-gradient(lightCyan, skyBlue, #6DCEF5); */
    border-bottom:1px skyBlue;
    box-shadow: 0px 2px 4px #6DCEF5;
    /* background-color: #6DCEF5; */
}

</style>
