<template>
  <div class="gx-room-content">
    <div class="videos-content" v-if="roomList.length">
      <div class="videos">
        <ThumbNail v-for="room in roomList" :key="room.id" :room="room">
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
.gx-room-content{
  height: 100%;
  display:flex;
  align-items: center;
}
.videos-content{
  font-style: normal;
  display: grid;
  grid-template-rows: 45% 45%;
  grid-template-columns: 32% 32% 30%;
  column-gap: 10px;
  row-gap: 30px;
}

.no-items {
  width: 100%;
  text-align: center;
  font-size: 1.25em;
  font-weight: 500;
}
</style>
