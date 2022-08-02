<template>
  <div class="grid-container">
    <FollowBar></FollowBar>
    <div class="header">
      <h1 class="gxroom">gx룸</h1>
      <h2 class="gxcommunity">gx커뮤니티</h2>
      <button class="createroom">방생성</button>
      <input class="search" placeholder="검색">
    </div>
    <div class="followbar">
    </div>
    <div class="thumbnail1"></div>
    <div class="thumbnail2"></div>
    <div class="thumbnail3"></div>
    <div class="thumbnail4"></div>
    <div class="thumbnail5"></div>
    <div class="thumbnail6"></div>
  </div>
</template>

<script>
import FollowBar from '../common/FollowBar.vue'
export default {
  components: { FollowBar }
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
    "followbar thumbnail1 thumbnail2 thumbnail3"
    "followbar thumbnail4 thumbnail5 thumbnail6";
  column-gap: 10px;
row-gap: 30px;
}
.header{
  margin: auto;
  grid-area: header;
}
.gxroom{
  margin-left: 400px;
  margin-top: 60px;
  float: left;
  font-size: 20px;
}
.gxcommunity{
  float: left;
  font-size: 20px;
  margin-top: 60px;
  margin-left: 200px;
}
.createroom{
  width: 80px;
  height: 30px;
  border: 2px solid #000000;
  border-radius: 15px;
  float: left;
  margin-top: 60px;
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
  margin-top: 60px;
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
.thumbnail1{
  margin:auto;
  grid-area: thumbnail1;
  box-sizing: border-box;
  width: 300px;
  height: 240px;
  background: url(http://cdn.kormedi.com/wp-content/uploads/2021/09/08_014.jpg);
  border: 1px solid #000000;
  border-radius: 20px;
}
.thumbnail2{
  margin:auto;
  grid-area: thumbnail2;
  box-sizing: border-box;
  width: 300px;
  height: 240px;
  background: url(http://cdn.kormedi.com/wp-content/uploads/2021/09/08_014.jpg);
  border: 1px solid #000000;
  border-radius: 20px;
}
.thumbnail3{
  margin:auto;
  grid-area: thumbnail3;
  box-sizing: border-box;
  width: 300px;
  height: 240px;
  background: url(http://cdn.kormedi.com/wp-content/uploads/2021/09/08_014.jpg);
  border: 1px solid #000000;
  border-radius: 20px;
}
.thumbnail4{
  margin:auto;
  grid-area: thumbnail4;
  box-sizing: border-box;
  width: 300px;
  height: 240px;
  background: url(http://cdn.kormedi.com/wp-content/uploads/2021/09/08_014.jpg);
  border: 1px solid #000000;
  border-radius: 20px;
}
.thumbnail5{
  margin:auto;
  grid-area: thumbnail5;
  box-sizing: border-box;
  width: 300px;
  height: 240px;
  background: url(http://cdn.kormedi.com/wp-content/uploads/2021/09/08_014.jpg);
  border: 1px solid #000000;
  border-radius: 20px;
}
.thumbnail6{
  margin:auto;
  grid-area: thumbnail6;
  box-sizing: border-box;
  width: 300px;
  height: 240px;
  background: url(http://cdn.kormedi.com/wp-content/uploads/2021/09/08_014.jpg);
  border: 1px solid #000000;
  border-radius: 20px;
}
</style>
