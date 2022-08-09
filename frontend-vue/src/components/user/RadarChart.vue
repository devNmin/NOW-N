<template>
  <div style="max-width: 150px">
    <vue3-chart-js v-bind="{ ...RadarChart }"/>
  </div>
</template>

<script>
import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'

export default {
  name: 'RadarChart',
  components: {
    Vue3ChartJs
  },
  setup () {
    const RadarChart = {
      type: 'radar',
      options: {
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
          y: {
            min: -100,
            max: 10,
            ticks: {
              callback: function (value) {
                return `${value}%`
              }
            }
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
              3,
              5,
              2,
              7,
              1,
              0
            ],
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)'
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
