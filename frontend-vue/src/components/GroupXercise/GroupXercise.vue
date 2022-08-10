<template>
  <div class="grid2">
    <div class="GX-header">
<<<<<<< HEAD
      <!-- 라우터 링크는 커뮤니티룸 만들고 난 이후에 추가하기 -->
      <!-- <router-link
            v-for="categoy in GXcategories" :key="category.link" :to="category.link">{{category.name}}
        </router-link> -->
      <h1 class="gxroom">gx룸</h1>
      <h2 class="gxcommunity">gx커뮤니티</h2>
      <button class="createroom">방생성</button>
      <input class="search" placeholder="검색">
    </div>
    <div class="videos">
      <div v-for="i in th" :key="i">
        <ThumbNail :src="i.roomsrc"></ThumbNail>
        {{ i.roomname }}
      </div>
=======
      <h1 class="gxroom">gx룸</h1>
      <h1 class="gxcommunity">gx커뮤니티</h1>
      <button type="button" @click="moveToRegist">방 생성</button>
      <router-link class="view-button" to="gx/conferences/1/">방입장</router-link>|
      <input class="search" placeholder="검색">
    </div>
    <div class="videos-content">
      <div class="videos" v-if="roomList.length">
        <ThumbNail v-for="room in roomList" :key="room.id" :room="room">
        </ThumbNail>
      </div>
      <div class="no-items" v-else>개설된 미팅룸이 없습니다.</div>
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD
import ThumbNail from '@/components/common/ThumbNail.vue'
=======
import ThumbNail from '@/components/GroupXercise/ThumbNail.vue'
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
export default {
  components: {
    ThumbNail
  },
  setup () {
<<<<<<< HEAD
    const th = [
      // roomsrc에다가 사진 주소 넣으면 썸네일 사진으로 사용가능
      { roomname: 'room1', roomsrc: 1 },
      { roomname: 'room2', roomsrc: 2 },
      { roomname: 'room3', roomsrc: 3 },
      { roomname: 'room4', roomsrc: 4 },
      { roomname: 'room5', roomsrc: 5 },
      { roomname: 'room6', roomsrc: 6 }
    ]
    // const GXcategories = [
    //   { name: 'gx룸', link: '/GX/getlist/' },
    //   { name: 'gx커뮤니티', link: '/pt' }
    // ]
    return {
      th
      // GXcategories
=======
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
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
    }
  }
}
</script>

<style scoped>
.grid2{
<<<<<<< HEAD
  font-family: 'MaruBuriOTF';
=======
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
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
<<<<<<< HEAD
=======
  font-family: 'MaruBuriOTF';
  font-style: normal;
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
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
<<<<<<< HEAD
.videos{
  grid-area: thumbnail;
  font-family: 'MaruBuriOTF';
=======
.videos-content{
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
  font-style: normal;
  display: grid;
  grid-template-rows: 50% 50%;
  grid-template-columns: 33.3% 33.3% 33.3%;
  column-gap: 10px;
row-gap: 30px;
}
<<<<<<< HEAD
=======

.no-items {
  height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.25em;
  font-weight: 500;
}
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
</style>
