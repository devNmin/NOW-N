<template>
    <div >
      <div class='navcontent'>
      <img src="@\assets\x.png" alt="Logo.png">
        <div class="nav1">
          <router-link
              v-for="item in commonItems" :key="item.link" :to="item.link">{{item.name}}
          </router-link>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  setup () {
    const commonItems = [
      { name: 'gx', link: '/GX' },
      { name: 'px', link: '/px' },
      { name: '트레이너', link: '/trainer' },
      { name: '로그인', link: '/login' }
    ]
    return { commonItems }
  }
}
</script>

<style scoped>
.nav1{
  display: flex;
  justify-content: flex-end;
  gap: 32px;
}
.navcontent{
    display: flex;
    height: 1rem;
    padding: 32px 64px;
    font-size: 1.1em;
    justify-content: space-between;
    background-color: #6DCEF5;
}
</style>
