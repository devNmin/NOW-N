<template>
  <div class="px-diary-gird" >
    <div class="px-diary-calendar" >
        <DatePicker class='calendarSt"' is-expanded
        :attributes='attributes'
          is-double-paned
          v-model='state.Nowdate' @click="testClick">
        </DatePicker>
    </div>
    <div>
    <h1>{{state.Nowdate.getMonth()+1}} 월 {{state.Nowdate.getDate()}} 일</h1>
    <div style="display: flex; justify-content: flex-end; margin-bottom: 30px; position: relative;
    top: -15px;">
      <button type="button" @click="RegistDiet">추가</button>
    </div>
    <div class="px-diary-info">
        <!-- <DietDiary v-for="diary in " -->
        <div class="diaryContent">
          <div class="diaryItem" v-for="(item, index ) in foodItems.diet_data" :key="index">
            <img style="border-radius: 20%; margin-right:10px" :src="item.picture" alt="" width="150" height="150">
            <div class="diaryText" >
              <h1 style="margin:0;">{{item.category}} </h1>
              <h2 style="margin:0;">
                <div v-if="item.time.slice(4, 6) == 'AM'">
                  오전{{item.time.slice(0, 2)}}:{{item.time.slice(2, 4)}} / {{item.total_calorie}} cal
                </div>
                <div v-else>
                  오후 {{item.time.slice(0, 2)}}:{{item.time.slice(2, 4)}} / {{item.total_calorie}} cal
                </div>
              </h2>
              <h3 style="margin:0;">{{item.comment}}</h3>
              <div style="display: flex; ">
              <div v-for="(food, fi)  in foodItems.foods_data[index]" :key="fi" >
                <div style='margin-left:20px;' class="diaryText" >{{food.name}} {{food.size}}g</div>
              </div>
              </div>
            </div>
          </div>
        </div>
    </div>
    </div>
  </div>
</template>

<script>
import { DatePicker } from 'v-calendar'
import { reactive, onMounted } from '@vue/runtime-core'
import { useRouter } from 'vue-router'
import axios from 'axios'
export default {
  components: {
    DatePicker
  },
  setup () {
    const foodItems = reactive({ diet_data: [], foods_data: [] })
    const router = useRouter()
    onMounted(() => {
      testClick()
    })
    async function testClick () {
      const year = state.Nowdate.getFullYear()
      const month = ('0' + (state.Nowdate.getMonth() + 1)).slice(-2)
      const day = ('0' + state.Nowdate.getDate()).slice(-2)
      const dateString = year + month + day
      console.log('dateStringdateString', dateString)
      await axios({
        url: 'http://127.0.0.1:8000/PX/todaydiets/' + dateString,
        method: 'get',
        headers: { Authorization: 'JWT ' + localStorage.accessToken }
      }).then(res => {
        const a = res.data

        foodItems.foods_data = a.foods_data
        foodItems.diet_data = a.diet_data
        // console.log(rightItems.diet_data)
        console.log(foodItems)
      }
      )
    }

    function RegistDiet () {
      router.push({ name: 'createDiet' })
    }
    const state = reactive({ test: 'zxc', Nowdate: new Date(), testBase: '' })
    const attributes = [
      {
        // bar: {
        //   color: 'red'// Purple bar
        // },
        bar: {
          color: 'red'// Purple bar
        },
        // highlight: 'red',
        dates: [
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
        // bar: {
        //   color: 'red'// Purple bar
        // },
        bar: {
          color: 'blue'// Purple bar
        },
        // highlight: 'red',
        dates: [
          new Date(2022, 7, 12), // Jan 12th
          new Date(2022, 7, 26), // Jan 26th
          new Date(2022, 7, 15), // Jan 15th
          new Date(2022, 7, 5) // Feb 5t
        ]
      }
    ]
    return { attributes, state, RegistDiet, testClick, foodItems }
  }
}
</script>

<style scoped>

.button-container{
  display:block;
  margin:auto;
  /* display:inline-block; */
}
button{
  /* background-color: var(--color-grey-900); */
  color: #6dcef5;

  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border-width: 0;
  width: 70px;
  height: 30px;
  font-size: 20px;
  text-align: center;
  font-weight: bold;
}

button:hover {
  background-color: #6dcef5;
  color: white;
  font-weight: bold;
}

button.disabled{
  cursor: default;
  background-color: var(--color-grey-100);
  border: 2px solid var(--color-grey-500);
  color: var(--color-grey-500);
}

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
  height: 50vh;
}

</style>
