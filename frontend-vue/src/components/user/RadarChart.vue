<template>
  <div style="max-width: 500px; display: flex;
  align-items: center;">
    <vue3-chart-js v-bind="{ ...RadarChart }"/>
  </div>
</template>

<script>
import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'
import { useStore } from 'vuex'
export default {
  name: 'RadarChart',
  components: {
    Vue3ChartJs
  },
  setup () {
    const store = useStore()
    const UserInfoP = store.state.profile.UserInfo
    const RadarChart = {
      type: 'radar',
      options: {
        ticks: { min: 0, max: 10, stepSize: 2 },
        maintainAspectRatio: false,
        min: 0,
        max: 10,
        responsive: true,
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
          ticks: {
            maxTicksLimit: 3,
            display: false
          },
          r: {
            angleLines: {
              display: false
            },
            suggestedMin: 0,
            suggestedMax: 10
          }
        }
      },
      data: {
        labels: [
          '요가',
          '필라테스',
          '맨몸운동',
          '스트레칭',
          '기구운동',
          '기타'
        ],
        datasets: [
          {
            label: '운동 정보',
            data: [
              UserInfoP.exercise.Yoga,
              UserInfoP.exercise.Pilates,
              UserInfoP.exercise.FullBody,
              UserInfoP.exercise.Stretching,
              UserInfoP.exercise.Machine,
              UserInfoP.exercise.Etc
            ],
            borderColor: 'rgba(255, 99, 132, 0.5)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
            pointBackgroundColor: 'rgba(109, 206 ,245, 0.7)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(54, 162, 235)'
          }
        ]
      }
    }

    return {
      RadarChart
    }
  }
}
</script>
