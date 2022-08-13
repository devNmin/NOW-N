<template>
  <FollowBar></FollowBar>
  <div class="GX-container">
    <div class="GX-grid">
      <div class="GX-menu">
        <button type="button" class='graphBtn' @click="moveToRegist" >방 생성</button>
      </div>
      <div class="GX-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>
<script>
import { useRouter } from 'vue-router'

import FollowBar from '@/components/common/FollowBar.vue'
export default {
  components: {
    FollowBar
  },

  setup () {
    const gxItems = [
      { name: 'gxRoom', link: '/GX/conferences', title: 'G.X 룸' },
      { name: 'comunity', link: '/GX/community', title: '커뮤니티' }
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
.graphBtn{
  justify-items: center;
  color: #6dcef5;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border-width: 0;
  font-size: 15px;
  text-align: center;
  font-weight: bolder;
  margin-left:550px;
}
.GX-container{
  height: 85%;
  position: relative;
  width: 85%;
  left: 15%;
}
.GX-grid{
  display: grid;
  width:100%;
  height:100%;
  grid-template-rows: 1fr 7fr;
  position: relative;
  left: 150px;
  top: 15px;
}

.GX-menu{
  display: flex;
  align-items: center;
  margin: 20px 20px 20px 0px;
  gap: 50px;
}
.GX-content{
  height: 100%;
  width: 70%;
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

.make-btn:hover{
  /* background-color: #F4F4F4; */
  background-color: black;
}

</style>
