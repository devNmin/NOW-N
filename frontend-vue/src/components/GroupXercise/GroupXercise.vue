<template>
  <div class="grid2">
    <div class="GX-header">
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
    </div>
  </div>
</template>

<script>
import ThumbNail from '@/components/common/ThumbNail.vue'
export default {
  components: {
    ThumbNail
  },
  setup () {
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
    }
  }
}
</script>

<style scoped>
.grid2{
  font-family: 'MaruBuriOTF';
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
.videos{
  grid-area: thumbnail;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  display: grid;
  grid-template-rows: 50% 50%;
  grid-template-columns: 33.3% 33.3% 33.3%;
  column-gap: 10px;
row-gap: 30px;
}
</style>
