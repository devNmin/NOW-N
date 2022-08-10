<template>
    <div class="calendar">
        <h2 class="calendar-nav">
            <a href="#" v-on:click="onClickPrev(currentMonth)">◁</a>
            {{ currentYear }}년 {{ currentMonth }}월
            <a href="#" v-on:click="onClickNext(currentMonth)">▷</a>
        </h2>
        <table class="table table-hover">
            <thead>
                <tr>
                    <td v-for="(weekName, index) in weekNames" v-bind:key="index">
                        {{ weekName }}
                    </td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, index) in currentCalendarMatrix" :key="index">
                    <td v-for="(day, index2) in row" :key="index2" style="padding:20px;">
                        <span v-if="isToday(currentYear, currentMonth, day)" class="rounded">
                            {{ day }}
                        </span>
                        <span v-else>
                            {{ day }}
                        </span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div>
        <CChartRadar :data="{
    labels: [
      'Eating',
      'Drinking',
      'Sleeping',
      'Designing',
      'Coding',
      'Cycling',
      'Running',
    ],
    datasets: [
      {
        label: 'My First dataset',
        backgroundColor: 'rgba(220, 220, 220, 0.2)',
        borderColor: 'rgba(220, 220, 220, 1)',
        pointBackgroundColor: 'rgba(220, 220, 220, 1)',
        pointBorderColor: '#fff',
        pointHighlightFill: '#fff',
        pointHighlightStroke: 'rgba(220, 220, 220, 1)',
        data: [65, 59, 90, 81, 56, 55, 40],
      },
      {
        label: 'My Second dataset',
        backgroundColor: 'rgba(151, 187, 205, 0.2)',
        borderColor: 'rgba(151, 187, 205, 1)',
        pointBackgroundColor: 'rgba(151, 187, 205, 1)',
        pointBorderColor: '#fff',
        pointHighlightFill: '#fff',
        pointHighlightStroke: 'rgba(151, 187, 205, 1)',
        data: [28, 48, 40, 19, 96, 27, 100],
      },
    ],
  }" />
    </div>
</template>

<script>
export default {
  name: 'CalendarView',
  data () {
    return {
      weekNames: ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일'],
      rootYear: 1904,
      rootDayOfWeekIndex: 4, // 2000년 1월 1일은 토요일
      currentYear: new Date().getFullYear(),
      currentMonth: new Date().getMonth() + 1,
      currentDay: new Date().getDate(),
      currentMonthStartWeekIndex: null,
      currentCalendarMatrix: [],
      endOfDay: null,
      memoDatas: []
    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init: function () {
      this.currentMonthStartWeekIndex = this.getStartWeek(this.currentYear, this.currentMonth)
      this.endOfDay = this.getEndOfDay(this.currentYear, this.currentMonth)
      this.initCalendar()
    },
    initCalendar: function () {
      this.currentCalendarMatrix = []
      let day = 1
      for (let i = 0; i < 6; i++) {
        const calendarRow = []
        for (let j = 0; j < 7; j++) {
          if (i === 0 && j < this.currentMonthStartWeekIndex) {
            calendarRow.push('')
          } else if (day <= this.endOfDay) {
            calendarRow.push(day)
            day++
          } else {
            calendarRow.push('')
          }
        }
        this.currentCalendarMatrix.push(calendarRow)
      }
    },
    getEndOfDay: function (year, month) {
      switch (month) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
          return 31
        case 4:
        case 6:
        case 9:
        case 11:
          return 30
        case 2:
          if ((year % 4 === 0) && (year % 100 !== 0)) {
            return 29
          } else if (year % 400 === 0) {
            return 29
          } else {
            return 28
          }
        default:
          console.log('unknown month ' + month)
          return 0
      }
    },
    getStartWeek: function (targetYear, targetMonth) {
      let year = this.rootYear
      let month = 1
      let sumOfDay = this.rootDayOfWeekIndex
      while (true) {
        if (targetYear > year) {
          for (let i = 0; i < 12; i++) {
            sumOfDay += this.getEndOfDay(year, month + i)
          }
          year++
        } else if (targetYear === year) {
          if (targetMonth > month) {
            sumOfDay += this.getEndOfDay(year, month)
            month++
          } else if (targetMonth === month) {
            return (sumOfDay) % 7
          }
        }
      }
    },
    onClickPrev: function (month) {
      month--
      if (month <= 0) {
        this.currentMonth = 12
        this.currentYear -= 1
      } else {
        this.currentMonth -= 1
      }
      this.init()
    },
    onClickNext: function (month) {
      month++
      if (month > 12) {
        this.currentMonth = 1
        this.currentYear += 1
      } else {
        this.currentMonth += 1
      }
      this.init()
    },
    isToday: function (year, month, day) {
      const date = new Date()
      return year === date.getFullYear() && month === date.getMonth() + 1 && day === date.getDate()
    }
  }
}
</script>

<style type="text/css">

.rounded {
    border-radius: 20px 20px 20px 20px;
    border: solid 1px #ffffff;
    background-color: #2b6bd1;
    padding: 10px;
    color: #ffffff;
}

.calendar{
    background: #FFFFFF;
    box-shadow: 13.2087px 4.95327px 36.324px 16.5109px rgba(150, 150, 150, 0.11);
    border-radius: 26.4174px;
    width:500px;
    height:500px;
}

.calendar-nav{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0px 24px;
    gap: 93px;
}
.table {
  margin: auto;
}
</style>
