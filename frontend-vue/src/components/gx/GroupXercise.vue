<template>
  <div class="GX-grid">
    <div class="GX-menu">
          <div style="margin-right:650px"><h1>Group eXercise</h1></div>
          <div><SearchBar @search="search"/></div>
          <button type="button" class='crateRoombtn' @click="moveToRegist" >방 생성</button>
    </div>
    <div class="gx-room-content">
      <div class="videos-content" v-if="roomList.length">
        <div style="margin:10px; height:310px; width:80%;" v-for="room in roomList" :key="room.id">
          <ThumbNail :room="room">
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
  width:100%;
  height:100%;
  grid-template-rows: 80px 670px;
}

.GX-menu{
  display: flex;
  justify-content: flex-end;
  position: relative;
  align-items: center;
  gap: 50px;
  box-shadow: 10px 5px 5px gray;
}

.gx-room-content{
  display: flex;
  justify-content: center;
  align-items: center;
}
.crateRoombtn{
  margin-right: 50px;
  padding:10px;
  justify-items: center;
  background-color: white;
  color: #6dcef5;
  box-shadow: 0px 4 px 4px rgba(0, 0, 0, 0.25);
  border-radius: 20px;
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

.videos-content{
  display: grid;
  width:100%;
  height:670px;
  grid-template-rows: 1fr 1fr;
  grid-template-columns: 1fr 1fr 1fr;
}

.no-items {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.25em;
  font-weight: 500;
}
</style>
