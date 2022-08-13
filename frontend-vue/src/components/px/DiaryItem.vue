<template>
  <div class="diaryContent">
    <div class="diaryItem" v-for="item in rightItems" :key="item.link" :to="item.link">
      <img :src="item.url" alt="" width="150" height="150">
      <div class="diaryText">
        <div>{{item.moment}} {{item.time}}</div>
        <div>{{item.cal}}</div>
        <div>{{item.foods}}</div>
        <div>{{item.comments}}</div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    Nowdate: {
      type: Date
    }
  },
  setup () {
    const rightItems = [
      { url: require('@/assets/food4.jpg'), moment: '아침', time: '오전 10:3', cal: '500 ' + 'kcal', comments: '개빡친다', foods: '사과 배 참외' },
      { url: require('@/assets/food4.jpg'), moment: '저녁', time: '오후 7:25', cal: '250 ' + 'kcal', comments: '배부르다 진짜', foods: '햄버거 치킨 ' }
    ]

    return { rightItems }
  }
}
</script>

<style scoped>
.diaryItem {
    display: flex;
    margin-bottom: 0px;
}
.diaryText{
    display: flex;
    flex-direction: column;
    margin-bottom: 0;
}
</style>
