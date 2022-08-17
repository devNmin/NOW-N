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
    <div>
    <h1>{{state.Nowdate.getMonth()+1}} 월 {{state.Nowdate.getDate()}} 일</h1>
    <div class="px-diary-info">
        <!-- <DietDiary v-for="diary in " -->
        <div class="diaryContent">
          <div class="diaryItem" v-for="item in rightItems" :key="item.link" :to="item.link">
            <img style="border-radius: 20%; margin-right:10px" :src="item.url" alt="" width="150" height="150">
            <div class="diaryText" >
              <h1 style="margin:0;">{{item.moment}} </h1>
              <h2 style="margin:0;">
                <div v-if="item.time.slice(4, 6) == 'AM'">
                  오전{{item.time.slice(0, 2)}}:{{item.time.slice(2, 4)}} / {{item.cal}}
                </div>
                <div v-else>
                  오후 {{item.time.slice(0, 2)}}:{{item.time.slice(2, 4)}} / {{item.cal}}
                </div>
              </h2>
              <h3 style="margin:0;">{{item.comments}}</h3>
              <h4>{{item.foods}}</h4>
            </div>
          </div>
        </div>
        <!-- <DiaryItem
          v-bind:Nowdate="state.Nowdate">
        </DiaryItem> -->
        <button type="button" @click="RegistDiet">이미지 추가 버튼</button>
            <!-- v-model input에서 값을 받아올 이름 지정 -->
        <button @click="testClick" >test</button>
        <!-- <img src="data:image/png;base64,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" alt=""> -->
    </div>
    </div>
  </div>
</template>

<script>
import { DatePicker } from 'v-calendar'
import { reactive } from '@vue/runtime-core'
import { useRouter } from 'vue-router'
import axios from 'axios'
export default {
  components: {
    DatePicker
  },
  setup () {
    const rightItems = [
      { url: require('@/assets/food4.jpg'), moment: '아침', time: '1020AM', cal: '500 ' + 'kcal', comments: '개빡친다', foods: '사과 배 참외' },
      { url: require('@/assets/food4.jpg'), moment: '야식', time: '1150PM', cal: '250 ' + 'kcal', comments: '배부르다 진짜', foods: '햄버거 치킨 ' },
      { url: require('@/assets/food4.jpg'), moment: '저녁', time: '오후 7:40', cal: '250 ' + 'kcal', comments: '배부르다 진짜', foods: '햄버거 치킨 ' },
      { url: require('@/assets/food4.jpg'), moment: '저녁', time: '오후 7:40', cal: '250 ' + 'kcal', comments: '배부르다 진짜', foods: '햄버거 치킨 ' },
      { url: require('@/assets/food4.jpg'), moment: '저녁', time: '오후 7:40', cal: '250 ' + 'kcal', comments: '배부르다 진짜', foods: '햄버거 치킨 ' },
      { url: require('@/assets/food4.jpg'), moment: '저녁', time: '오후 7:40', cal: '250 ' + 'kcal', comments: '배부르다 진짜', foods: '햄버거 치킨 ' }
    ]
    const router = useRouter()

    function testClick () {
      axios({
        url: 'http://localhost:8001/test/',
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        console.log(res.data[0])
        // "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==";
        // data:image/png;base64,
        // state.testBase = 'data:image/png;base64,' + res.data
        state.testBase = 'data:image/png;base64,' + `${res.data}`
        // state.testBase = 'data:image/png;base64,' + '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'
        console.log('asdasd', 'data:image/jpg;base64,' + res.data[0])
        console.log('asdasd', 'data:image/jpg;base64,' + res.data)
        const image = document.getElementById('my-image')
        console.log('imageimageimageimageimage', image)
        // image.src = 'data:image/png;base64,' + `${res.data}`
      }
      )
    }

    function RegistDiet () {
      router.push({ name: 'createDiet' })
    }

    const state = reactive({ test: 'zxc', Nowdate: new Date(), testBase: '' })
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
    return { attributes, state, RegistDiet, testClick, rightItems }
  }
}
</script>

<style scoped>
.diaryItem {
    display: flex;
    margin-bottom: 15px;
}
.diaryText{
    display: flex;
    flex-direction: column;
    margin-bottom: 0;
}
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
  overflow-y:scroll;
  height: 70vh;
}

</style>
