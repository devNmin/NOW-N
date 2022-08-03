<template>
  <div class="grid-container">
    <FollowBar></FollowBar>
    <div class="header">
      <h1 class="gxroom">gx룸</h1>
      <h2 class="gxcommunity">gx커뮤니티</h2>
      <button class="createroom">방생성</button>
      <input class="search" placeholder="검색">
    </div>

    <div class="videos">
      <div v-for="i in th" :key="i">
        <ThumbNail></ThumbNail>
      </div>
    </div>
  </div>
</template>

<script>
import FollowBar from '../common/FollowBar.vue'
import ThumbNail from '../common/ThumbNail.vue'
export default {
  components: {
    FollowBar,
    ThumbNail
  },
  setup () {
    const th = [1, 2, 3, 4, 5, 6]
    return {
      th
    }
  }
}
</script>

<style>
.grid-container{
  /* height:1400px; */
  font-family: 'MaruBuriOTF';
  font-style: normal;
  display: grid;
  grid-template-rows: 20% 40% 40%;
  grid-template-columns: 22% 26% 26% 26%;
  grid-template-areas:
    "header header header header"
    "followbar thumbnail thumbnail thumbnail"
    "followbar thumbnail thumbnail thumbnail";
  column-gap: 10px;
row-gap: 30px;
}
.header{
  margin: auto;
  grid-area: header;
}
.gxroom{
  margin-left: 400px;
  margin-top: 100px;
  float: left;
  font-size: 20px;
}
.gxcommunity{
  float: left;
  font-size: 20px;
  margin-top: 100px;
  margin-left: 200px;
}
.createroom{
  width: 80px;
  height: 30px;
  border: 2px solid #000000;
  border-radius: 15px;
  float: left;
  margin-top: 100px;
  margin-left: 300px;
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
  margin-top: 100px;
  margin-left: 50px;
}
input{
  width: 100%;
  padding: 10px;
}
.followbar{
  margin: auto;
  grid-area: followbar;
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
