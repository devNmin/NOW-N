<template>
  <div class="px-diary-content">
    <div class="px-diary-calendar">
      <Calendar></Calendar>
    </div>
    <div class="px-diary-info">
        <h1>8월 8일</h1>
        <!-- <DietDiary v-for="diary in " -->
        <DietDiary></DietDiary>
        <button type="button">이미지 추가 버튼</button>
    </div>
  </div>>
</template>

<script>
import Calendar from '../common/Calendar.vue'
import DietDiary from '@/components/px/DiaryItem.vue'
export default {
  components: { Calendar, DietDiary }
}
</script>

<style scoped>
.px-diary-content{
  display:grid;
  width: 100vw;
  height: 100vh;
  grid-template-columns: 1fr 1fr;
}

.px-diary-calendar{
  margin: auto;
}

.px-diary-info{
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
}

.px-diary-info h1{
  font-size: 3em;
  font-weight: 600;
  color: #6DCEF5;
}
</style>
