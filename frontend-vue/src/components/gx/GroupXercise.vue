<template>
  <div class="gx-room-content">
    <div class="videos-content" v-if="roomList.length">
      <div class="videos">
        <ThumbNail style="margin-left:50px;" v-for="room in roomList" :key="room.id" :room="room">
        </ThumbNail>
      </div>
    </div>
    <div class="no-items" v-else>개설된 미팅룸이 없습니다.</div>
  </div>
</template>

<script>
import ThumbNail from '@/components/gx/ThumbNail.vue'
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  components: {
    ThumbNail
  },
  setup () {
    const store = useStore()

    const roomList = computed(() => store.state.room.roomList)

    return {
      roomList
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
