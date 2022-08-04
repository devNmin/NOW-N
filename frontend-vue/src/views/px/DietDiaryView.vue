<template>
  <div class="container">
    <div class="grid-container">
      <div>
        <BaseHeader></BaseHeader>
      </div>
      <div>
        <FollowBar></FollowBar>
      </div>
      <div>
        <DietDiary></DietDiary>
      </div>
    </div>
  </div>
</template>

<script>
import BaseHeader from '@/components/common/BaseHeader.vue'
import FollowBar from '@/components/common/FollowBar.vue'
import DietDiary from '@/components/px/DietDiary.vue'
export default {
  component: {
    DietDiary,
    BaseHeader,
    FollowBar
  }
}
</script>

<style scoped>
.container{
  height : 1600px;
}
/* .grid-container{
  font-family: 'MaruBuriOTF';
  font-style: normal;
  display: grid;
  grid-template-rows: 10% 90%;
  grid-template-columns: 25% 75%;
  grid-template-areas:
    "B-header B-header"
    "F-bar D-Diary";
  column-gap: 10px;
row-gap: 30px;
} */
/* .B-header{
  margin: 0;
  grid-area: B-header;
}
.F-bar{
  margin: 0;
  grid-area: F-bar;
}
.D-Diary{
  margin: 0;
  grid-area: D-Diary;
} */
</style>>
