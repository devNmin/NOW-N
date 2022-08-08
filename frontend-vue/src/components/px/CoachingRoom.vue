<template>
  <div class="grid-container-coachingroom">
    <div class="B-header">
      <BaseHeader></BaseHeader>
    </div>
    <div class="F-bar">
      <FollowBar></FollowBar>
    </div>
    <div class="D-category">
      <h1 class="category-diary">
        <router-link to="/PT/diet/getcalorie/">식단 다이어리</router-link>
      </h1>
      <h2 class="category-coaching">
        <router-link to="/PT/graph/date/">체중 그래프</router-link>
      </h2>
      <h3 class="category-graph">
        <router-link to="/PT/onetoone/enterroom/">1:1 코칭룸</router-link>
      </h3>
    </div>
    <div class="body">
      <div class="grid2">
        <h4 class="coachinfo">
          <div class="coachinfobox">

          </div>
        </h4>
        <h5 class="schedule">
          <div class="schedulebox"></div>
        </h5>
        <h6 class="community">
          <div class="communitybox"></div>
        </h6>
        <h7 class="counselinfo">
          <div class="counselinfobox"></div>
        </h7>
      </div>
    </div>
  </div>
</template>

<script>
import BaseHeader from '@/components/common/BaseHeader.vue'
import FollowBar from '@/components/common/FollowBar.vue'
export default {
  components: {
    BaseHeader,
    FollowBar
  }
}
</script>

<style scoped>
.grid-container-coachingroom {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  display: grid;
  grid-template-rows: 5% 5% 90%;
  grid-template-columns: 25% 75%;
  grid-template-areas:
    "B-header B-header"
    "F-bar D-category"
    "F-bar body";
  column-gap: 10px;
  row-gap: 30px;
  height: 1500px;
}
.B-header{
  margin: 0;
  grid-area: B-header;
}
.F-bar{
  margin: 0;
  grid-area: F-bar;
}
.D-category{
  margin: 0;
  grid-area: D-category;
  float: left;
}
.category-diary{
  margin-left: 7vw;
  margin-top: 0;
  float: left;
  font-size: 3vh;
}
.category-coaching{
  margin-left: 12vw;
  margin-top: 0;
  float: left;
  font-size: 3vh;
}
.category-graph{
  margin-left: 12vw;
  margin-top: 0;
  float: left;
  font-size: 3vh;
}
.body{
  margin: 0;
  grid-area: body;
}
.grid2 {
  display: grid;
  grid-template-rows: 20% 20% 60%;
  grid-template-columns: 65% 45%;
  grid-template-areas:
    "coachinfo schedule"
    "community schedule"
    "counselinfo counselinfo";
  column-gap: 10px;
  row-gap: 30px;
  height: 1200px;
}
.coachinfo {
  margin: 0;
  grid-area: coachinfo;
}
.coachinfobox {
  margin-bottom: 10vh;
  margin-top: 0;
  width: 40vw;
  height: 30vh;
  background: #FFFFFF;
}
.schedule {
  margin: 0;
  grid-area: schedule;
}
.schedulebox {
  width: 21.5vw;
  height: 70vh;
  background: #FFFFFF;
}
.community {
  margin: 0;
  grid-area: community;
}
.communitybox {
  width: 40vw;
  height: 30vh;
  background: #FFFFFF;
}
.counselinfo {
  margin: 0;
  grid-area: counselinfo;
}
.counselinfobox{
  width: 70vw;
  height: 30vh;
  background: #FFFFFF;
}
</style>
