<template>
  <div class="GX-container">
    <div class="GX-grid">
      <div class="GX-menu">
        <router-link class="menu-item"
          v-for="item in gxItems" :key="item.link" :to="item.link"> {{ item.title }}
        </router-link>
        <img src="@/assets/v.png" class="make-btn" @click="moveToRegist" />
        <SearchBar></SearchBar>
      </div>
      <div class="GX-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>
<script>
import { useRouter } from 'vue-router'
import SearchBar from '@/components/common/SearchBar.vue'

export default {
  components: {
    SearchBar
  },

  setup () {
    const gxItems = [
      { name: 'gxRoom', link: '/GX/conferences', title: 'G.X 룸' },
      { name: 'comunity', link: '/GX/conferences', title: '커뮤니티' }
    ]

    const router = useRouter()

    function moveToRegist () {
      router.push({ name: 'createConference' })
    }

    return { gxItems, moveToRegist }
  }
}
</script>
<style scoped>
.GX-container{
  /* height: calc(100vh - 86px); */
  height: 100%;
}
.GX-grid{
  display: grid;
  width:100%;
  height:100%;
  grid-template-rows: 1fr 7fr;
}

.GX-menu{
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

.make-btn{
  height:50px;
  width:50px;
  margin-left:750px;
  cursor: pointer;
}

.make-btn:hover{
  /* background-color: #F4F4F4; */
  background-color: black;
}

.GX-content{
  height: 100%;
  /* height: calc(100vh-124px); */
}
</style>
