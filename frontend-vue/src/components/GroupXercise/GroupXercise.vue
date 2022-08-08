<template>
  <div class="grid2">
    <div class="GX-header">
      <h1 class="gxroom">gx룸</h1>
      <h1 class="gxcommunity">gx커뮤니티</h1>
      <router-link class="view-button" to="gx/conferences/1/">방입장</router-link>|
      <input class="search" placeholder="검색">
    </div>
    <div class="videos-content">
      <div class="videos" v-if="roomList.length">
        <ThumbNail v-for="room in roomList" :key="room.id" :room="room">
        </ThumbNail>
      </div>
      <div class="no-items" v-else>개설된 미팅룸이 없습니다.</div>
    </div>
  </div>
</template>

<script>
import ThumbNail from '@/components/common/ThumbNail.vue'
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

export default {
  components: {
    ThumbNail
  },
  setup () {
    const store = useStore()
    const router = useRouter()

    const roomList = computed(() => store.state.room.roomList)

    function moveToRegist () {
      router.push({ name: 'createConference' })
    }

    return {
      roomList, moveToRegist
    }
  },
  async created () {
    try {
      this.$store.dispatch('getRoomList')
    } catch (e) {
      alert('서버에 문제가 발생하였습니다')
    }
  }
}
</script>

<style scoped>
.grid2{
  font-style: normal;
  display: grid;
  grid-template-rows: 10% 90%;
  grid-template-areas:
    "GX-header"
    "thumbnail";
  column-gap: 10px;
row-gap: 30px;
}
.GX-header{
  margin: 0;
  grid-area: GX-header;
}
.gxroom{
  margin-left: 5vw;
  float: left;
  font-size: 20px;
}
.gxcommunity{
  float: left;
  font-size: 20px;
  margin-left: 10vw;
}
.createroom{
  width: 80px;
  height: 30px;
  border: 2px solid #000000;
  border-radius: 15px;
  float: left;
  margin-top: 2vh;
  margin-left: 20vw;
  background: #6dcef5;
  color: white;
}
button:hover {
  background-color: var(--color-grey-900);
  color: white;
}
.search{
  box-sizing: border-box;
  background: #FFFFFF;
  border: 1px solid #000000;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
  width: 300px;
  height: 30px;
  float: left;
  margin-top: 2vh;
  margin-left: 1vw;
}
input{
  width: 100%;
  padding: 10px;
}
.videos-content{
  font-style: normal;
  display: grid;
  grid-template-rows: 50% 50%;
  grid-template-columns: 33.3% 33.3% 33.3%;
  column-gap: 10px;
row-gap: 30px;
}

.no-items {
  height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.25em;
  font-weight: 500;
}
</style>
