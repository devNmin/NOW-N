<template>
  <div>
  <h1 class="label-box">Phone Number</h1>
  <div style="height: 10px;"></div>
    <div class="Birth-page">
      <div id="bir_yy">
          <span class="box">
              <input type="text" v-model="date.yyyy" class="input-Birth-box" maxlength="4" placeholder="년(4자)">
          </span>
      </div>
      <div class="birth-margin-box"></div>
      <div id="bir_mm">
        <span>
          <select v-model="date.mm" class="input-Birth-box select-box-border" @change="changeMonth">
            <option>월</option>
            <option v-for="month in date.months"
              :key="month"
             :value="month">{{month}}월</option>
          </select>
        </span>
      </div>

      <div class="birth-margin-box"></div>
      <div id="bir_dd">
        <span>
          <select v-model="date.dd" class="input-Birth-box select-box-border" @change="onChange">
            <option>일</option>
            <option v-for="day in date.days"
              :key="day"
             :value="day">{{day}}일</option>
          </select>
        </span>
      </div>
    </div>
    <span class="error_next_box"></span>
  </div>
</template>

<script>
import { reactive, computed } from 'vue'
export default {
  setup (props, { emit }) {
    const date = reactive({
      first: '',
      second: '',
      third: '',
      phone_number: computed(() => birthChange()),
      months: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
      days: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    })
    function birthChange () {
      console.log('birthChange')
      return date.yyyy + date.mm + date.dd
    }
    function changeMonth (event) {
      if (event.target.value === '01' || event.target.value === '03' || event.target.value === '05' || event.target.value === '07' || event.target.value === '08' || event.target.value === '10' || event.target.value === '12') {
        date.days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
      } else if (event.target.value === '04' || event.target.value === '06' || event.target.value === '09' || event.target.value === '11') {
        date.days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
      } else {
        date.days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
      }
    }
    function onChange (event) {
      console.log('메렁' + date.birth)
      emit('birth', date.birth)
    }

    return {
      date,
      onChange,
      changeMonth
    }
  }
}
</script>

<style>
.Birth-page {
  display: flex;
  justify-content: center;
  margin: auto;
}

.birth-margin-box {
  width: 30px;
}
.input-Birth-box {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
  border: 0px;
  background-color: none;
  border-bottom: solid 2px #6dcef5;
  border-radius: 2px;
  width: 80px;
  height: 45px;
  margin: auto;
  font-size: 20px;
  padding-left: 20px;
  padding: 0px;
}
.select-box-border {
 height: 47px;
}
</style>