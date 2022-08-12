<template>
  <div class="PX-container">
    <div class="PX-grid">
      <div class="PX-menu">
        <router-link class="menu-item"
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
  height: 100%;
}
.PX-grid{
  display: grid;
  width: 100%;
  height: 100%;
  grid-template-rows: 1fr 7fr;
}

.PX-menu{
  display: flex;
  align-items: center;
  margin: 20px 20px 20px 100px;
  gap: 100px;
}

.menu-item{
  margin: 30px;
  text-decoration: none;
  display: flex;
  align-items: center;
  font-weight: bolder;
  font-size:1.5rem;
  color: black;
}

.PX-content{
  height:100%;
}
</style>>
