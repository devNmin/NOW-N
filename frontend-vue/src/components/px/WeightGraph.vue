<template>
  <div class="grid-container-weightgraph">
    <div class="B-header">
      <BaseHeader></BaseHeader>
    </div>
    <div class="FollowBar">
      <FollowBar></FollowBar>
    </div>
    <div class="body">
      <div class="grid-container-body">
        <div class="category">
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
        <div class="dailybutton">
          <button class="B-button">
            일별
          </button>
          <button class="B-button">
            주별
          </button>
          <button class="B-button">
            월별
          </button>
        </div>
        <div class="graph">
          <h4 class="graphbox"></h4>
        </div>
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
.grid-container-weightgraph {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  display: grid;
  grid-template-rows: 5% 95%;
  grid-template-columns: 25% 75%;
  grid-template-areas:
    "B-header B-header"
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
.body{
  margin: 0;
  grid-area: body;
}
.grid-container-body{
  display: grid;
  grid-template-rows: 5% 5% 90%;
  grid-template-areas:
    "category"
    "dailybutton"
    "graph";
  column-gap: 10px;
  row-gap: 30px;
  height: 1500px;
}
.category{
  margin: 0;
  grid-area: category;
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
.dailybutton{
  margin: 0;
  grid-area: dailybutton;
}
.B-button{
  width: 5vw;
  height: 5vh;
  border: 2px solid #000000;
  border-radius: 15px;
  float: left;
  margin-top: 0;
  margin-left: 12vw;
  background: #6dcef5;
  color: white;
}
button:hover {
  background-color: var(--color-grey-900);
  color: white;
}
.graph{
  margin: 0;
  grid-area: graph;
}
.graphbox{
  width: 60vw;
  height: 60vh;
  background: #FFFFFF;
}
</style>
