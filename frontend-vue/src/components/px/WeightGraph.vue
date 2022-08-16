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
import { reactive } from 'vue'
export default {
  components: { LineChart },
  setup () {
    const caoptions = [
      { id: 'bmi', value: 'bmi 지수' },
      { id: 'kcal', value: '칼로리' },
      { id: 'nutrient', value: '영양소' }
    ]
    const cyoptions = [
      { id: 'daily', value: '일별' },
      { id: 'weekly', value: '주별' },
      { id: 'montly', value: '월별' }
    ]
    const data = reactive({
      cycle: '',
      category: ''
    })

    return { data, caoptions, cyoptions }
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
