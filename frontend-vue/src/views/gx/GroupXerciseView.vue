<template>
  <div class="box">
    <div class="grid-container">
        <div class="B-header">
          <BaseHeader></BaseHeader>
        </div>
      <div class="F-bar">
        <FollowBar></FollowBar>
      </div>
      <div class="G-exercise">
        <GroupXercise></GroupXercise>
      </div>
    </div>
  </div>
</template>
<script>
import GroupXercise from '@/components/GroupXercise/GroupXercise.vue'
import BaseHeader from '@/components/common/BaseHeader.vue'
import FollowBar from '@/components/common/FollowBar.vue'
export default {
  components: {
    BaseHeader,
    GroupXercise,
    FollowBar
  }
}
</script>
<style scoped>
.box{
  height: 1500px;
}
.grid-container{
  font-family: 'MaruBuriOTF';
  font-style: normal;
  display: grid;
  grid-template-rows: 10% 90%;
  grid-template-columns: 25% 75%;
  grid-template-areas:
    "B-header B-header"
    "F-bar G-exercise";
  column-gap: 10px;
row-gap: 30px;
}
.B-header{
  margin: 0;
  grid-area: B-header;
}
.F-bar{
  margin: 0;
  grid-area: F-bar;
}
.G-exercise{
  margin: 0;
  grid-area: G-exercise;
}
</style>
