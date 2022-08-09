<template>
    <nav>
        <router-link
            v-for="item in commonItems" :key="item.link" :to="item.link">{{item.name}}
        </router-link>
    </nav>
</template>

<script>
export default {
  setup () {
    const commonItems = [
      { name: 'gx', link: '/GX' },
      { name: 'pt', link: '/pt' },
      { name: '트레이너', link: '/trainer' },
      { name: '로그인', link: '/login' }
    ]
    return { commonItems }
  }
}
</script>

<style scoped>
nav{
    display: flex;
    gap: 32px;
    font-size: 1.1em;
}
</style>
