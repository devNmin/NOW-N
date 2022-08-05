<template>
  <div class="grid-container-diet-diary">
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
    <div class="Date">
      <div>
        1월 2일
      </div>
    </div>
    <div class="D-diary">
      <div class="grid2">
        <h4 class="calendar">
        </h4>
        <h5>
          <div class="diary" v-for="i in ds" :key="i">
          </div>
        </h5>
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
  },
  setup () {
    const ds = [1, 2, 3]
    return {
      ds
    }
  }
}
</script>

<style scoped>
.grid-container-diet-diary{
  font-family: 'MaruBuriOTF';
  font-style: normal;
  display: grid;
  grid-template-rows: 5% 5% 5% 80%;
  grid-template-columns: 25% 35% 40%;
  grid-template-areas:
    "B-header B-header B-header"
    "F-bar D-category D-category"
    "F-bar Date Date"
    "F-bar D-diary D-diary";
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
.Date{
  margin-top: 0;
  margin-left: 30vw;
  grid-area: Date;
  font-size: 3vh;
}
.D-diary{
  margin: 0;
  grid-area: D-diary;
}
.grid2{
  display: grid;
  grid-template-rows: 40% 60%;
  grid-template-columns: 50% 50%;
  grid-template-areas:
    "calendar diary"
    "calendar diary";
  column-gap: 10px;
  row-gap: 30px;
  height: 1300px;
}
.calendar{
  margin: 0;
  grid-area: calendar;
  width: 30vw;
  height: 70vh;
  background: #FFFFFF;
}
.diary{
  margin-bottom: 10vh;
  margin-top: 0;
  grid-area: diary;
  width: 30vw;
  height: 30vh;
  background: #FFFFFF;
}
</style>
