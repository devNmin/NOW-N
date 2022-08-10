<template>
  <div class="PX-container">
    <div class="PX-grid">
      <div class="PX-menu">
        <router-link
          v-for="item in pxItems" :key="item.name" :to="item.link">{{item.title}}
        </router-link>
      </div>
      <div class="PX-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  setup () {
    const pxItems = [
      { name: 'pxDiaries', link: '/PX/Diaries', title: '식단 다이어리' },
      { name: 'pxGraph', link: '/PX/graph', title: '체중 그래프' },
      { name: 'pxCoaching', link: '/PX/coaching', title: '1:1 코칭룸' }
    ]

    return { pxItems }
  }
}
</script>

<style scoped>
.PX-container{
  display: flex;
}
.PX-grid{
  display: grid;
  width: 100vw;
  height: 100vh;
  grid-template-rows: 1fr 7fr;
  grid-template-areas:
  "px-menu"
  "px-content";
}

.PX-menu{
  grid-area: px-menu;
  display: flex;
  gap: 50px;
}

.PX-content{
  grid-area: px-content;
}
</style>>
