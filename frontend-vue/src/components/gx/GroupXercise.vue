<template>
  <div class="GX-grid">
  <div class="GX-menu">
        <div><SearchBar @search="search"/></div>
        <button type="button" class='crateRoombtn' @click="moveToRegist" >방 생성</button>
  </div>
  <div class="gx-room-content">
    <div class="videos-content" v-if="roomList.length">
      <div class="videos">
        <ThumbNail style="margin-left:50px;" v-for="room in roomList" :key="room.id" :room="room">
        </ThumbNail>
      </div>
    </div>
    <div class="no-items" v-else>개설된 미팅룸이 없습니다.</div>
  </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router'
import ThumbNail from '@/components/gx/ThumbNail.vue'
import SearchBar from '@/components/common/SearchBar.vue'
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  components: {
    ThumbNail, SearchBar
  },
  setup () {
    const store = useStore()
    const roomList = computed(() => store.state.room.roomList)
    const router = useRouter()

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
.GX-grid{
  display: grid;
  width:85%;
  height:100%;
  grid-template-rows: 1fr 7fr;
  position: relative;
  left: 150px;
  top: 15px;
}
.gx-room-content{
  display: flex;
}
.crateRoombtn{
  justify-items: center;
  background-color: white;
  color: #6dcef5;
  box-shadow: 0px 4 px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border-width: 0;
  font-size: 15px;
  text-align: center;
  font-weight: bolder;
}
.crateRoombtn:hover{
  /* background-color: #F4F4F4; */
  background-color: #6dcef5;
  color: white;
}
.GX-menu{
  display: flex;
  justify-content: flex-end;
  position: relative;
  align-items: center;
  left: 0%;
  margin: 20px 20px 20px 0px;
  gap: 50px;
}

.videos-content{
  margin-left:-20px ;
}
.videos {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  position: relative;
  left: 70px;
  top: 10px;
}

.no-items {
  width: 100%;
  text-align: center;
  font-size: 1.25em;
  font-weight: 500;
}
</style>
