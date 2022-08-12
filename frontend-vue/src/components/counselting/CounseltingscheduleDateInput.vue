<template>
  <div>
    <div class="split-page2">
      <div>
        <span>
          <select v-model="date.mm" class="schedule-input-split-box schedule-select-box-border" @change="changeMonth">
            <option v-for="month in date.months"
              :key="month"
             :value="month">{{month}}월</option>
          </select>
        </span>
      </div>

      <div class="schedule-split-margin-box">/</div>
      <div>
        <span>
          <select v-model="date.dd" class="schedule-input-split-box schedule-select-box-border" @change="onChange" placeholder="일">
            <option v-for="day in date.days"
              :key="day"
             :value="day">{{day}}일</option>
          </select>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, computed } from 'vue'
export default {
  setup (props, { emit }) {
    const date = reactive({
      mm: '01',
      dd: '01',
      scedule: computed(() => sceduleChange()),
      months: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
      days: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    })
    function sceduleChange () {
      return date.mm + '.' + date.dd
    }
    function changeMonth (event) {
      if (event.target.value === '01' || event.target.value === '03' || event.target.value === '05' || event.target.value === '07' || event.target.value === '08' || event.target.value === '10' || event.target.value === '12') {
        date.days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
      } else if (event.target.value === '04' || event.target.value === '06' || event.target.value === '09' || event.target.value === '11') {
        date.days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
      } else {
        date.days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
      }
      emit('update:modelValue', date.scedule)
    }
    function onChange (event) {
      emit('update:modelValue', date.scedule)
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
.split-page2 {
  display: flex;
  justify-content: center;
  margin: auto;
  border-bottom: solid 1px #6dcef5;

}

.schedule-split-margin-box {
  display: flex;
  width: 30px;
  justify-content: center;
  align-items : center;
}
.schedule-input-split-box {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
  border: 0px;
  border-radius: 2px;
  width: 60px;
  height: 45px;
  margin: auto;
  font-size: 20px;
  padding-left: 20px;
  padding: 0px;
}
.schedule-select-box-border {
 height: 47px;
}
</style>
