<template>
  <div class="GX-container">
    <div class="GX-grid">
      <div class="GX-menu">
        <router-link class="menu-item"
          v-for="item in gxItems" :key="item.link" :to="item.link"> {{ item.title }}
        </router-link>
        <div>
          <img src="@/assets/v.png" class="make-btn" @click="moveToRegist" />
          <p class="arrow_box">방송하기</p>
        </div>
        <input class="search" placeholder="검색">
      </div>
      <div class="GX-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  setup () {
    const gxItems = [
      { name: 'gxRoom', link: '/GX/conferences', title: 'G.X 룸' },
      { name: 'comunity', link: '/GX/conferences', title: '커뮤니티' }
    ]

    return { gxItems }
  }
}
</script>
<style scoped>
.GX-container{
  /* height: calc(100vh - 86px); */
  height: 100%;
}
.GX-grid{
  display: grid;
  width:100vw;
  height:100%;
  grid-template-rows: 1fr 7fr;
}

.GX-menu{
  display: flex;
  align-items: center;
  margin: 20px 20px 20px 100px;
  gap: 100px;
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

.make-btn{
  height:50px;
  width:50px;
  margin-left:750px;
  cursor: pointer;
}

.arrow-box{
  display: none;
  position: absolute;
  width:100px;
  padding: 8px;
  -webkit-border-radius: 8px;
  -moz-border-radius: 8px;
  border-radius: 8px;
  background: #333;
  color: #fff;
  font-size: 14px;
}

.arrow_box:after {
  position: absolute;
  bottom: 100%;
  left: 50%;
  width: 0;
  height: 0;
  margin-left: -10px;
  border: solid transparent;
  border-color: rgba(51, 51, 51, 0);
  border-bottom-color: #333;
  border-width: 10px;
  pointer-events: none;
  content: ' ';
}

.make-btn:hover + p.arrow_box {
  display: block;
}

.search{
  font-family: 'MaruBuriOTF';
  font-style: normal;
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

.GX-content{
  height: 100%;
  /* height: calc(100vh-124px); */
}
</style>
