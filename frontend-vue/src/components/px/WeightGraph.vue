<template>
  <div class="diet-graph-container">
    <div class="graph-cycle">
      싸이클
    </div>
    <div class="graph-category">
      카테고리
    </div>
    <div class="graph">
      <LineChart></LineChart>
    </div>
  </div>
</template>

<script>
import LineChart from '@/components/px/Chart/LineChart.vue'

export default {
  components: {
    LineChart
  },
  data () {
    return {
      datacollection: null
    }
  },
  created () {
    this.fillData()
  },
  methods: {
    fillData () {
      this.datacollection = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            // Data for the x-axis of the chart
            data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
          }
        ]
      }
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  }
}
</script>

<style scoped>
.diet-graph-container{
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: 1fr 5fr;
  grid-template-rows: 1fr 4fr;
  grid-template-areas:
  "graph-cycle graph-cycle"
  "graph-category graph"
}

.graph-cycle{
  grid-area: graph-cycle;
  display: flex;
  justify-content: center;
  align-content: center;
}

.graph-category{
  grid-area: graph-category;
  display: flex;
  justify-content: center;
  align-content: center;
}

.graph{
  grid-area: graph;
  display: flex;
  justify-content: center;
  align-content: center;
}
</style>
