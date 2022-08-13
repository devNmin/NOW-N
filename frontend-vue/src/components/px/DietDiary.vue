<template>
  <div class="px-diary-gird" >
    <div class="px-diary-calendar" >
        <DatePicker class='calendarSt' is-expanded
        :attributes='attributes'
          is-double-paned
          v-model='state.Nowdate'>
        </DatePicker>
        <div class="px-diary-text">
          간단한 문구 1달 간단한 운동기록 보여줘도좋고
        </div>
    </div>
    <div class="px-diary-info">
        <h3>{{state.Nowdate.getMonth()+1}} 월 {{state.Nowdate.getDate()}} 일</h3>
        <!-- <DietDiary v-for="diary in " -->
        <DiaryItem
          v-bind:Nowdate="state.Nowdate">
        </DiaryItem>
        <button type="button" @click="RegistDiet">이미지 추가 버튼</button>
            <!-- v-model input에서 값을 받아올 이름 지정 -->
    </div>
  </div>
</template>

<script>
import DiaryItem from '@/components/px/DiaryItem.vue'
import { DatePicker } from 'v-calendar'
import { reactive } from '@vue/runtime-core'
import { useRouter } from 'vue-router'
export default {
  components: {
    DiaryItem, DatePicker
  },
  setup () {
    const router = useRouter()

    function RegistDiet () {
      router.push({ name: 'createDiet' })
    }

    const state = reactive({ test: 'zxc', Nowdate: new Date() })
    const attributes = [
      {
        bar: {
          backgroundColor: '#ff4d4d' // Red bar
        },
        dates: [
          new Date(2018, 0, 1), // Jan 1st
          new Date(2018, 0, 10), // Jan 10th
          new Date(2018, 0, 22), // Jan 22nd
          new Date(2018, 1, 6), // Feb 6th
          new Date(2018, 1, 16) // Feb 16h
        ]
      },
      {
        bar: {
          backgroundColor: 'blue'// Turquoise bar
        },
        dates: [
          new Date(2022, 7, 4), // Jan 4th
          new Date(2022, 7, 10), // Jan 10th
          new Date(2022, 8, 15), // Jan 15th
          new Date(2022, 8, 1), // Feb 1st
          new Date(2022, 8, 12), // Feb 12th
          {
            start: new Date(2022, 8, 20), // Feb 20th
            end: new Date(2022, 8, 25)// - Feb 25th
          }
        ]
      },
      {
        // bar: {
        //   color: 'red'// Purple bar
        // },
        bar: {
          color: 'red'// Purple bar
        },
        // highlight: 'red',
        dates: [
          new Date(2022, 7, 12), // Jan 12th
          new Date(2022, 7, 26), // Jan 26th
          new Date(2022, 7, 15), // Jan 15th
          new Date(2022, 7, 5), // Feb 5th
          new Date(2022, 7, 6), // Feb 6th
          new Date(2022, 7, 9), // Feb 9th
          new Date(2022, 7, 20), // Feb 20th
          new Date(2022, 7, 25), // Feb 25th
          {
            start: new Date(2022, 7, 28), // Feb 20th
            end: new Date(2022, 7, 30)// - Feb 25th
          }
        ]
      },
      {
        dot: {
          backgroundColor: 'red'
        },
        popover: {
          label: state.test
        },
        dates: [
          new Date(2022, 7, 23)
        ]
      }
    ]
    return { attributes, state, RegistDiet }
  }
}
</script>

<style scoped>
.px-diary-gird{
  display: grid;
  grid-template-columns: 40% 60%;
  height: 100%;
  grid-template-areas:
  "px-diary-calendar px-diary-info"

}
.px-diary-calendar{
  display: flex;
  flex-direction: column;
  margin: auto 0;
}
.px-diary-text{
  margin-top: 50px;
}
.calendarSt{
  display: flex;
  justify-content: center;
  justify-items: center;
}
.px-diary-content {
  display: flex;
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
